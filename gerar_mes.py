from pathlib import Path
from datetime import date
import calendar
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
# MESES E DIAS DA SEMANA
# ============================================================

MESES_PTBR = {
    1: "JANEIRO",
    2: "FEVEREIRO",
    3: "MARÇO",
    4: "ABRIL",
    5: "MAIO",
    6: "JUNHO",
    7: "JULHO",
    8: "AGOSTO",
    9: "SETEMBRO",
    10: "OUTUBRO",
    11: "NOVEMBRO",
    12: "DEZEMBRO",
}


DIAS_SEMANA_PTBR = {
    0: "Seg",
    1: "Ter",
    2: "Qua",
    3: "Qui",
    4: "Sex",
    5: "Sáb",
    6: "Dom",
}


# ============================================================
# CORES
# ============================================================

COR_AMARELA = (255, 255, 0)
COR_CINZA = (166, 166, 166)
COR_BRANCA = (255, 255, 255)


# ============================================================
# CONSTANTES DO EXCEL
# ============================================================

XL_CENTER = -4108
XL_CONTINUOUS = 1
XL_THIN = 2

XL_EDGE_LEFT = 7
XL_EDGE_TOP = 8
XL_EDGE_BOTTOM = 9
XL_EDGE_RIGHT = 10
XL_INSIDE_VERTICAL = 11
XL_INSIDE_HORIZONTAL = 12


ABAS_IGNORADAS = [
    "TESTE PYTHON",
]


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def encontrar_arquivo(prefixo):
    arquivos = list(PASTA_TRABALHO.glob(f"{prefixo}*.xls*"))

    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo Excel encontrado começando com '{prefixo}' "
            f"na pasta: {PASTA_TRABALHO}"
        )

    return arquivos[0]


def nome_aba_mes(mes, ano):
    return f"{MESES_PTBR[mes]} {ano}"


def escolher_aba_base(wb):
    for sheet in reversed(wb.sheets):
        if sheet.name not in ABAS_IGNORADAS:
            return sheet

    raise Exception("Nenhuma aba base válida encontrada.")


def aplicar_bordas_range(rng, internas=False):
    bordas = [
        XL_EDGE_LEFT,
        XL_EDGE_TOP,
        XL_EDGE_BOTTOM,
        XL_EDGE_RIGHT,
    ]

    if internas:
        bordas += [
            XL_INSIDE_VERTICAL,
            XL_INSIDE_HORIZONTAL,
        ]

    for borda in bordas:
        try:
            rng.api.Borders(borda).LineStyle = XL_CONTINUOUS
            rng.api.Borders(borda).Weight = XL_THIN
        except Exception:
            pass


def formatar_celula_na(celula):
    celula.value = "N/A"

    try:
        celula.api.HorizontalAlignment = XL_CENTER
        celula.api.VerticalAlignment = XL_CENTER

        # Texto vertical
        celula.api.Orientation = 90

        # Fonte maior
        celula.api.Font.Name = "Times New Roman"
        celula.api.Font.Size = 18
        celula.api.Font.Bold = True

        celula.api.ShrinkToFit = False
        celula.api.WrapText = False
    except Exception:
        pass


def deve_pintar_amarelo(linha, dia_semana, config):
    """
    Verifica se determinada linha deve ser pintada de amarelo,
    de acordo com as regras específicas da planilha.

    Se a planilha não tiver regras específicas, retorna None.
    """

    regras = config.get("regras_preenchimento")

    if not regras:
        return None

    regra = regras.get(linha)

    if regra is None:
        return False

    tipo = regra.get("tipo")

    # Segunda a sexta
    if tipo == "dias_uteis":
        return dia_semana in [0, 1, 2, 3, 4]

    # Dias específicos da semana
    if tipo == "dias_semana":
        return dia_semana in regra.get("dias", [])

    # Todos os dias existentes
    if tipo == "todos":
        return True

    return False


def pintar_coluna_planejamento(ws, config, coluna, cor_cabecalho, dia_semana=None, dia_existe=True):
    """
    Pinta:
    - número do dia sempre cinza;
    - nome do dia da semana sempre cinza;
    - área das atividades conforme regra.

    Se a planilha não tiver regra específica:
    - mantém comportamento antigo na área das atividades:
      dias úteis amarelos, sábado/domingo cinza.

    Se tiver regra específica:
    - pinta somente as atividades configuradas.
    """

    linha_numero_dia = config["linha_numero_dia"]
    linha_dia_semana = config["linha_dia_semana"]
    linha_inicio = config["linha_inicio_preenchimento"]
    linha_fim = config["linha_fim_preenchimento"]

    # Cabeçalho dos dias SEMPRE cinza
    ws.range((linha_numero_dia, coluna)).color = COR_CINZA
    ws.range((linha_dia_semana, coluna)).color = COR_CINZA

    regras = config.get("regras_preenchimento")

    # Se não tiver regra específica:
    # dias úteis ficam amarelos na área toda, finais de semana ficam cinza
    if not regras:
        ws.range(
            (linha_inicio, coluna),
            (linha_fim, coluna)
        ).color = cor_cabecalho
        return

    # Se for sábado/domingo ou dia inexistente:
    # área toda fica cinza
    if not dia_existe or dia_semana in [5, 6]:
        ws.range(
            (linha_inicio, coluna),
            (linha_fim, coluna)
        ).color = COR_CINZA
        return

    # Se for dia útil e tiver regra específica:
    # pinta somente as atividades configuradas
    for linha in range(linha_inicio, linha_fim + 1):
        pintar = deve_pintar_amarelo(linha, dia_semana, config)

        if pintar:
            ws.range((linha, coluna)).color = COR_AMARELA
        else:
            ws.range((linha, coluna)).color = COR_BRANCA


def limpar_linhas_responsaveis(ws, config):
    coluna_inicial = config["coluna_inicial_dias"]
    coluna_final = coluna_inicial + 30

    linha_execucao = config["linha_responsavel_execucao"]
    linha_verificacao = config["linha_responsavel_verificacao"]

    ws.range(
        (linha_execucao, coluna_inicial),
        (linha_execucao, coluna_final)
    ).value = ""

    ws.range(
        (linha_verificacao, coluna_inicial),
        (linha_verificacao, coluna_final)
    ).value = ""


def preparar_linha_execucao(ws, config, dias_cinza):
    linha = config["linha_responsavel_execucao"]
    coluna_inicial = config["coluna_inicial_dias"]
    coluna_final = coluna_inicial + 30

    rng_execucao = ws.range(
        (linha, coluna_inicial),
        (linha, coluna_final)
    )

    try:
        rng_execucao.api.UnMerge()
    except Exception:
        pass

    rng_execucao.value = ""

    aplicar_bordas_range(rng_execucao, internas=True)

    for dia in dias_cinza:
        coluna = coluna_inicial + dia - 1
        celula = ws.range((linha, coluna))

        formatar_celula_na(celula)
        aplicar_bordas_range(celula, internas=False)


def preparar_linha_verificacao(ws, config, dias_cinza):
    linha = config["linha_responsavel_verificacao"]
    coluna_inicial = config["coluna_inicial_dias"]
    coluna_final = coluna_inicial + 30

    rng_verificacao = ws.range(
        (linha, coluna_inicial),
        (linha, coluna_final)
    )

    try:
        rng_verificacao.api.UnMerge()
    except Exception:
        pass

    rng_verificacao.value = ""

    dia = 1

    while dia <= 31:
        if dia in dias_cinza:
            coluna = coluna_inicial + dia - 1
            celula = ws.range((linha, coluna))

            formatar_celula_na(celula)
            aplicar_bordas_range(celula, internas=False)

            dia += 1
            continue

        inicio_bloco = dia

        while dia <= 31 and dia not in dias_cinza:
            dia += 1

        fim_bloco = dia - 1

        coluna_inicio_bloco = coluna_inicial + inicio_bloco - 1
        coluna_fim_bloco = coluna_inicial + fim_bloco - 1

        rng_bloco = ws.range(
            (linha, coluna_inicio_bloco),
            (linha, coluna_fim_bloco)
        )

        if coluna_fim_bloco > coluna_inicio_bloco:
            try:
                rng_bloco.api.Merge()
            except Exception:
                pass

        aplicar_bordas_range(rng_bloco, internas=False)


def ajustar_altura_linhas_responsaveis(ws, config):
    """
    Ajusta altura das linhas onde ficam assinatura/N/A.
    Pode ser personalizado por planilha no config_planilhas.py.
    """

    linha_execucao = config["linha_responsavel_execucao"]
    linha_verificacao = config["linha_responsavel_verificacao"]
    linha_supervisao = config["linha_responsavel_supervisao"]

    altura_execucao = config.get("altura_linha_execucao", 60)
    altura_verificacao = config.get("altura_linha_verificacao", 60)
    altura_supervisao = config.get("altura_linha_supervisao", 60)

    ws.range(f"{linha_execucao}:{linha_execucao}").row_height = altura_execucao
    ws.range(f"{linha_verificacao}:{linha_verificacao}").row_height = altura_verificacao
    ws.range(f"{linha_supervisao}:{linha_supervisao}").row_height = altura_supervisao


# ============================================================
# FUNÇÃO PRINCIPAL DO CALENDÁRIO
# ============================================================

def atualizar_calendario(ws, config, mes, ano):
    """
    Atualiza o calendário:
    - mês/ano;
    - dias;
    - dias da semana;
    - cores;
    - N/A;
    - responsáveis.

    Agora também respeita regras específicas de preenchimento,
    caso existam no config da planilha.
    """

    ultimo_dia = calendar.monthrange(ano, mes)[1]

    celula_mes_ano = config["celula_mes_ano"]
    linha_numero_dia = config["linha_numero_dia"]
    linha_dia_semana = config["linha_dia_semana"]
    coluna_inicial = config["coluna_inicial_dias"]

    dias_cinza = []

    # Atualiza cabeçalho
    ws.range(celula_mes_ano).value = f"Mês/Ano :              {MESES_PTBR[mes]}- {ano}"

    for dia in range(1, 32):
        coluna = coluna_inicial + dia - 1

        celula_dia = ws.range((linha_numero_dia, coluna))
        celula_semana = ws.range((linha_dia_semana, coluna))

        if dia <= ultimo_dia:
            data_atual = date(ano, mes, dia)
            dia_semana = data_atual.weekday()

            celula_dia.value = dia
            celula_semana.value = DIAS_SEMANA_PTBR[dia_semana]

            if dia_semana in [5, 6]:
                dias_cinza.append(dia)

                pintar_coluna_planejamento(
                    ws,
                    config,
                    coluna,
                    COR_CINZA,
                    dia_semana=dia_semana,
                    dia_existe=True
                )
            else:
                pintar_coluna_planejamento(
                    ws,
                    config,
                    coluna,
                    COR_AMARELA,
                    dia_semana=dia_semana,
                    dia_existe=True
                )

        else:
            limpar_dia_inexistente(ws, config, coluna)
            dias_cinza.append(dia)

            pintar_coluna_planejamento(
                ws,
                config,
                coluna,
                COR_CINZA,
                dia_semana=None,
                dia_existe=False
            )

    limpar_linhas_responsaveis(ws, config)
    preparar_linha_execucao(ws, config, dias_cinza)
    preparar_linha_verificacao(ws, config, dias_cinza)
    ajustar_altura_linhas_responsaveis(ws, config)


# ============================================================
# PROCESSAR UMA PLANILHA
# ============================================================

def processar_planilha(prefixo, mes, ano, app):
    config = CONFIG_PLANILHAS[prefixo]

    caminho_entrada = encontrar_arquivo(prefixo)
    nova_aba_nome = nome_aba_mes(mes, ano)

    nome_saida = f"{prefixo} - {nova_aba_nome}{caminho_entrada.suffix}"
    caminho_saida = PASTA_SAIDA / nome_saida

    print("")
    print("=" * 60)
    print(f"Processando planilha {prefixo}")
    print(f"Arquivo selecionado: {caminho_entrada.name}")
    print(f"Nova aba: {nova_aba_nome}")
    print(f"Arquivo será salvo em: {caminho_saida}")

    wb = None

    try:
        wb = app.books.open(str(caminho_entrada))

        nomes_abas = [sheet.name for sheet in wb.sheets]

        if nova_aba_nome in nomes_abas:
            print(f"A aba {nova_aba_nome} já existe. Apagando para criar novamente...")
            wb.sheets[nova_aba_nome].delete()

        aba_base = escolher_aba_base(wb)

        print(f"Aba base usada: {aba_base.name}")

        aba_base.api.Copy(After=wb.sheets[-1].api)

        nova_aba = wb.sheets.active
        nova_aba.name = nova_aba_nome

        atualizar_calendario(nova_aba, config, mes, ano)

        wb.save(str(caminho_saida))
        wb.close()

        print(f"OK: {nome_saida}")

    except Exception as erro:
        print(f"ERRO na planilha {prefixo}:")
        print(erro)

        try:
            if wb is not None:
                wb.close()
        except Exception:
            pass


# ============================================================
# EXECUÇÃO
# ============================================================

def main():
    print("")
    print("GERADOR DE CRONOGRAMAS")
    print("")

    print("Planilhas disponíveis:")
    print(", ".join(CONFIG_PLANILHAS.keys()))
    print("Ou digite TODOS para gerar todas.")
    print("")

    escolha = input("Digite a planilha desejada. Exemplo 01, 06 ou TODOS: ").strip().upper()

    try:
        mes = int(input("Digite o mês que deseja gerar. Exemplo 10 para outubro: "))
        ano = int(input("Digite o ano. Exemplo 2026: "))
    except ValueError:
        print("Mês e ano precisam ser números.")
        return

    if mes < 1 or mes > 12:
        print("Mês inválido. Digite um número de 1 a 12.")
        return

    if escolha == "TODOS":
        prefixos = list(CONFIG_PLANILHAS.keys())
    else:
        if escolha not in CONFIG_PLANILHAS:
            print(f"Planilha {escolha} não encontrada na configuração.")
            return

        prefixos = [escolha]

    app = xw.App(visible=True)
    app.display_alerts = False
    app.screen_updating = True

    try:
        for prefixo in prefixos:
            processar_planilha(prefixo, mes, ano, app)

        print("")
        print("Processo finalizado!")

    finally:
        app.quit()


if __name__ == "__main__":
    main()