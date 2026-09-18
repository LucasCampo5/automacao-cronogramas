from pathlib import Path
import xlwings as xw


ROOT = Path(__file__).resolve().parents[1]
PASTA_TRABALHO = ROOT / "arquivos_trabalho"


MESES = [
    "JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
    "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO",
    "Mês/Ano", "MÊS/ANO", "Mes/Ano", "MES/ANO"
]


def numero_para_coluna(numero):
    letras = ""

    while numero:
        numero, resto = divmod(numero - 1, 26)
        letras = chr(65 + resto) + letras

    return letras


def encontrar_arquivo(prefixo):
    arquivos = list(PASTA_TRABALHO.glob(f"{prefixo}*.xls*"))

    if not arquivos:
        print(f"Nenhum arquivo encontrado começando com {prefixo}")
        return None

    return arquivos[0]


def diagnosticar():
    prefixo = input("Digite o número da planilha. Exemplo 01, 02, 06: ").strip()

    caminho_arquivo = encontrar_arquivo(prefixo)

    if caminho_arquivo is None:
        return

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

        # Analisa a última aba
        ws = wb.sheets[-1]

        print("")
        print(f"Aba analisada: {ws.name}")

        used = ws.used_range
        ultima_linha = used.last_cell.row
        ultima_coluna = used.last_cell.column

        print(f"Última linha usada: {ultima_linha}")
        print(f"Última coluna usada: {numero_para_coluna(ultima_coluna)}")

        print("")
        print("Procurando células com texto de mês/ano...")

        for linha in range(1, ultima_linha + 1):
            for coluna in range(1, ultima_coluna + 1):
                valor = ws.range((linha, coluna)).value

                if isinstance(valor, str):
                    texto = valor.upper()

                    if any(mes.upper() in texto for mes in MESES):
                        endereco = f"{numero_para_coluna(coluna)}{linha}"
                        print(f"- {endereco}: {valor}")

        print("")
        print("Procurando possíveis linhas dos números dos dias...")

        for linha in range(1, ultima_linha + 1):
            valores_linha = []

            for coluna in range(1, ultima_coluna + 1):
                valor = ws.range((linha, coluna)).value
                valores_linha.append(valor)

            for indice in range(len(valores_linha) - 4):
                trecho = valores_linha[indice:indice + 5]

                if trecho == [1, 2, 3, 4, 5]:
                    coluna_inicio = indice + 1
                    endereco = f"{numero_para_coluna(coluna_inicio)}{linha}"
                    print(f"- Sequência 1,2,3,4,5 encontrada começando em {endereco}")

        print("")
        print("Procurando linhas de responsáveis...")

        palavras_responsaveis = [
            "RESPONSÁVEL",
            "RESPONSAVEL",
            "EXECUÇÃO",
            "EXECUCAO",
            "VERIFICAÇÃO",
            "VERIFICACAO",
            "SUPERVISÃO",
            "SUPERVISAO",
        ]

        for linha in range(1, ultima_linha + 1):
            for coluna in range(1, ultima_coluna + 1):
                valor = ws.range((linha, coluna)).value

                if isinstance(valor, str):
                    texto = valor.upper()

                    if any(palavra in texto for palavra in palavras_responsaveis):
                        endereco = f"{numero_para_coluna(coluna)}{linha}"
                        print(f"- {endereco}: {valor}")

        wb.close()

    except Exception as erro:
        print("")
        print("Erro durante diagnóstico:")
        print(erro)

    finally:
        app.quit()


if __name__ == "__main__":
    diagnosticar()