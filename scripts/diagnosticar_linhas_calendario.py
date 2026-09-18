from pathlib import Path
import xlwings as xw


ROOT = Path(__file__).resolve().parents[1]
PASTA_TRABALHO = ROOT / "arquivos_trabalho"


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


def mostrar_linhas_calendario():
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

        ws = wb.sheets[-1]

        print("")
        print(f"Aba analisada: {ws.name}")

        used = ws.used_range
        ultima_coluna = used.last_cell.column

        print("")
        print("Analisando linhas 7 até 12:")
        print("")

        for linha in range(7, 13):
            print(f"===== LINHA {linha} =====")

            for coluna in range(1, ultima_coluna + 1):
                valor = ws.range((linha, coluna)).value

                if valor not in [None, ""]:
                    endereco = f"{numero_para_coluna(coluna)}{linha}"
                    print(f"{endereco}: {valor}")

            print("")

        print("")
        print("Procurando valores individuais de dias 1, 2, 3, 4, 5 em toda a planilha:")
        print("")

        for linha in range(1, used.last_cell.row + 1):
            for coluna in range(1, ultima_coluna + 1):
                valor = ws.range((linha, coluna)).value

                if str(valor).strip() in ["1", "1.0", "2", "2.0", "3", "3.0", "4", "4.0", "5", "5.0"]:
                    endereco = f"{numero_para_coluna(coluna)}{linha}"
                    print(f"{endereco}: {valor}")

        wb.close()

    except Exception as erro:
        print("")
        print("Erro durante diagnóstico:")
        print(erro)

    finally:
        app.quit()


if __name__ == "__main__":
    mostrar_linhas_calendario()