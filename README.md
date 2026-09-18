# Automação de Cronogramas de Limpeza

Projeto em Python desenvolvido para automatizar a criação e o preenchimento mensal de planilhas Excel usadas em cronogramas de limpeza.

## Objetivo

Reduzir o trabalho manual na atualização mensal de várias planilhas, automatizando tarefas repetitivas como:

- criação ou atualização de abas mensais;
- preenchimento dos dias do mês;
- preenchimento dos dias da semana;
- aplicação de marcações por cores conforme regras específicas;
- geração de arquivos de saída sem alterar os arquivos originais.

## Tecnologias utilizadas

- Python
- openpyxl
- Excel

## Estrutura do projeto

```txt
automacao_cronogramas/
│
├── gerar_mes.py
├── config_planilhasOK.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── scripts/
│   ├── config_planilhas.py
│   ├── diagnosticar_linhas_calendario.py
│   ├── diagnosticar_planilha.py
│   ├── extrair_regras_amarelo.py
│   ├── gerar_mes.py
│   └── teste_copiar_aba.py