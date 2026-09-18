from pathlib import Path
import xlwings as xw


print("Script iniciado...")


ROOT = Path(__file__).resolve().parents[1]

PASTA_TRABALHO = ROOT / "arquivos_trabalho"
PASTA_SAIDA = ROOT / "saida"

PREFIXO_ARQUIVO = "06"
NOME_NOVA_ABA = "TESTE PYTHON"


def copiar_ultima_aba():
    print("Função copiar_ultima_aba foi chamada.")

    print(f"Pasta do projeto: {ROOT}")
    print(f"Pasta de trabalho: {PASTA_TRABALHO}")
    print(f"Pasta de saída: {PASTA_SAIDA}")

    arquivos_excel = list(PASTA_TRABALHO.glob("*.xls*"))

    print("")
    print("Arquivos Excel encontrados na pasta arquivos_trabalho:")

    if arquivos_excel:
        for arquivo in arquivos_excel:
            print(f"- {arquivo.name}")
    else:
        print("Nenhum arquivo Excel encontrado.")
        return

    arquivos_encontrados = list(PASTA_TRABALHO.glob(f"{PREFIXO_ARQUIVO}*.xls*"))

    if not arquivos_encontrados:
        print("")
        print(f"ERRO: Nenhum arquivo encontrado começando com {PREFIXO_ARQUIVO}")
        return

    caminho_entrada = arquivos_encontrados[0]
    caminho_saida = PASTA_SAIDA / caminho_entrada.name

    print("")
    print(f"Arquivo selecionado: {caminho_entrada.name}")
    print(f"Arquivo será salvo em: {caminho_saida}")

    app = xw.App(visible=True)
    app.display_alerts = False
    app.screen_updating = True

    try:
        wb = app.books.open(str(caminho_entrada))

        print("")
        print("Arquivo aberto com sucesso.")
        print("Abas encontradas:")

        for sheet in wb.sheets:
            print(f"- {sheet.name}")

        nomes_abas = [sheet.name for sheet in wb.sheets]

        if NOME_NOVA_ABA in nomes_abas:
            print("")
            print("A aba TESTE PYTHON já existe. Apagando para criar novamente...")
            wb.sheets[NOME_NOVA_ABA].delete()

        aba_base = wb.sheets[-1]

        print("")
        print(f"Aba base usada: {aba_base.name}")
        print("Copiando aba...")

        aba_base.api.Copy(After=wb.sheets[-1].api)

        nova_aba = wb.sheets.active
        nova_aba.name = NOME_NOVA_ABA

        print(f"Nova aba criada: {nova_aba.name}")

        wb.save(str(caminho_saida))
        wb.close()

        print("")
        print("Teste finalizado com sucesso!")
        print(f"Arquivo salvo em: {caminho_saida}")

    except Exception as erro:
        print("")
        print("Deu erro durante a execução:")
        print(erro)

    finally:
        app.quit()
        print("Excel fechado.")


if __name__ == "__main__":
    copiar_ultima_aba()