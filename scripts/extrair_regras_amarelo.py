from pathlib import Path
import xlwings as xw

from config_planilhas import CONFIG_PLANILHAS


# ============================================================
# ENCONTRAR PASTA DO PROJETO
# ============================================================

def encontrar_pasta_projeto():
    caminho_atual = Path(__file__).resolve()

    for pasta in [caminho_atual.parent] + list(caminho_atual.parents):
        if (pasta / "arquivos_trabalho").exists():
            return pasta

    raise FileNotFoundError("Não encontrei a pasta 'arquivos_trabalho'.")


ROOT = encontrar_pasta_projeto()
PASTA_TRABALHO = ROOT / "arquivos_trabalho"
PASTA_SAIDA = ROOT / "saida"

PASTA_SAIDA.mkdir(exist_ok=True)


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

DIAS_SEMANA_MAP = {
    "SEG": 0,
    "TER": 1,
    "QUA": 2,
    "QUI": 3,
    "SEX": 4,
    "SÁB": 5,
    "SAB": 5,
    "DOM": 6,
}


DIAS_SEMANA_NOME = {
    0: "Seg",
    1: "Ter",
    2: "Qua",
    3: "Qui",
    4: "Sex",
    5: "Sáb",
    6: "Dom",
}


def encontrar_arquivo(prefixo):
    arquivos = list(PASTA_TRABALHO.glob(f"{prefixo}*.xls*"))

    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo Excel encontrado começando com '{prefixo}' "
            f"na pasta: {PASTA_TRABALHO}"
        )

    return arquivos[0]


def cor_eh_amarela(cor):
    """
    Verifica se a cor da célula parece amarelo.
    O xlwings retorna algo como (255, 255, 0).
    Usamos tolerância porque às vezes o Excel salva pequenas variações.
    """

    if cor is None:
        return False

    try:
        r, g, b = cor
        return r >= 220 and g >= 220 and b <= 80
    except Exception:
        return False


def normalizar_dia_semana(valor):
    if valor is None:
        return None

    texto = str(valor).strip().upper()

    # Remove possíveis pontos
    texto = texto.replace(".", "")

    return DIAS_SEMANA_MAP.get(texto)


def detectar_regra(dias_semana_amarelos):
    """
    Tenta sugerir uma regra com base nos dias da semana encontrados.
    """

    dias_set = sorted(set(dias_semana_amarelos))

    if dias_set == [0, 1, 2, 3, 4]:
        return '{"tipo": "dias_uteis"}'

    if dias_set:
        return f'{{"tipo": "dias_semana", "dias": {dias_set}}}'

    return None


def extrair_regras():
    prefixo = input("Digite o número da planilha. Exemplo 04, 05, 07: ").strip()

    if prefixo not in CONFIG_PLANILHAS:
        print(f"Planilha {prefixo} não está no config_planilhas.py")
        return

    config = CONFIG_PLANILHAS[prefixo]

    caminho_arquivo = encontrar_arquivo(prefixo)

    print("")
    print(f"Arquivo selecionado: {caminho_arquivo.name}")

    app = xw.App(visible=True)
    app.display_alerts = False

    try:
        wb = app.books.open(str(caminho_arquivo))

        print("")
        print("Abas encontradas:")
        for i, sheet in enumerate(wb.sheets, start=1):
            print(f"{i} - {sheet.name}")

        print("")
        nome_aba = input("Digite o nome da aba correta para analisar. Enter = última aba: ").strip()

        if nome_aba:
            if nome_aba not in [s.name for s in wb.sheets]:
                print(f"Aba '{nome_aba}' não encontrada.")
                wb.close()
                return
            ws = wb.sheets[nome_aba]
        else:
            ws = wb.sheets[-1]

        print("")
        print(f"Aba analisada: {ws.name}")

        linha_inicio = config["linha_inicio_preenchimento"]
        linha_fim = config["linha_fim_preenchimento"]
        linha_dia_semana = config["linha_dia_semana"]
        coluna_inicial = config["coluna_inicial_dias"]

        resultado_linhas = []

        print("")
        print("=" * 70)
        print(f"REGRAS DETECTADAS PARA A PLANILHA {prefixo}")
        print("=" * 70)

        for linha in range(linha_inicio, linha_fim + 1):
            # Tenta pegar nome da atividade em algumas colunas possíveis
            valores_nome = []
            for col_nome in range(1, coluna_inicial):
                valor = ws.range((linha, col_nome)).value
                if valor not in [None, ""]:
                    valores_nome.append(str(valor).strip())

            nome_atividade = " | ".join(valores_nome) if valores_nome else f"Linha {linha}"

            dias_amarelos = []
            dias_semana_amarelos = []

            for dia in range(1, 32):
                coluna = coluna_inicial + dia - 1

                celula = ws.range((linha, coluna))
                cor = celula.color

                if cor_eh_amarela(cor):
                    valor_semana = ws.range((linha_dia_semana, coluna)).value
                    dia_semana = normalizar_dia_semana(valor_semana)

                    dias_amarelos.append(dia)

                    if dia_semana is not None:
                        dias_semana_amarelos.append(dia_semana)

            if dias_amarelos:
                regra_sugerida = detectar_regra(dias_semana_amarelos)

                print("")
                print(f"Linha {linha}: {nome_atividade}")
                print(f"Dias amarelos: {dias_amarelos}")
                print(
                    "Dias da semana amarelos: "
                    + ", ".join(DIAS_SEMANA_NOME[d] for d in sorted(set(dias_semana_amarelos)))
                )
                print(f"Regra sugerida: {regra_sugerida}")

                resultado_linhas.append((linha, nome_atividade, regra_sugerida))

        print("")
        print("=" * 70)
        print("BLOCO PARA COLAR NO config_planilhas.py")
        print("=" * 70)
        print('"regras_preenchimento": {')

        for linha, nome_atividade, regra in resultado_linhas:
            if regra:
                print(f"    {linha}: {regra},  # {nome_atividade}")

        print("},")

        # Salva também num arquivo TXT na pasta saida
        caminho_txt = PASTA_SAIDA / f"regras_detectadas_{prefixo}.txt"

        with open(caminho_txt, "w", encoding="utf-8") as arquivo_txt:
            arquivo_txt.write(f"REGRAS DETECTADAS PARA A PLANILHA {prefixo}\n\n")
            arquivo_txt.write('"regras_preenchimento": {\n')

            for linha, nome_atividade, regra in resultado_linhas:
                if regra:
                    arquivo_txt.write(f"    {linha}: {regra},  # {nome_atividade}\n")

            arquivo_txt.write("},\n")

        print("")
        print(f"Arquivo TXT salvo em: {caminho_txt}")

        wb.close()

    except Exception as erro:
        print("")
        print("Erro ao extrair regras:")
        print(erro)

    finally:
        app.quit()


if __name__ == "__main__":
    extrair_regras()