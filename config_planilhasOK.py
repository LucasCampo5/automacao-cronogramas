CONFIG_PLANILHAS = {
    "01": {
        "celula_mes_ano": "B7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 7,  # G
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_uteis"},  # RETIRAR LIXO
            12: {"tipo": "dias_uteis"},  # LIMPEZA DA MOBÍLIA
            13: {"tipo": "dias_uteis"},  # LIMPEZA GERAL DOS ARMÁRIOS
            14: {"tipo": "dias_uteis"},  # LIMPEZA DO CHÃO
            15: {"tipo": "dias_uteis"},  # RETIRADA DE TEIA DE ARANHA
        },
    },

    "02": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,
    },

    "03": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_uteis"},  # RETIRAR LIXO
            12: {"tipo": "dias_uteis"},  # LIMPEZA DA MOBÍLIA
            13: {"tipo": "dias_semana", "dias": [1, 3, 4]},  # TER, QUI, SEX
            14: {"tipo": "dias_uteis"},  # LIMPEZA DO CHÃO
            15: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            16: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
        },
    },

    "04": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_uteis"},  # RETIRAR LIXO
            12: {"tipo": "dias_uteis"},  # LIMPEZA DA MOBÍLIA
            13: {"tipo": "dias_semana", "dias": [1, 3]},  # TERÇA E QUINTA
            14: {"tipo": "dias_uteis"},  # LIMPEZA DO CHÃO
            15: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            16: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
        },
    },

    "05": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_uteis"},  # VERIFICAR TEIA DE ARANHA
            12: {"tipo": "dias_uteis"},  # RETIRAR LIXO
            13: {"tipo": "dias_uteis"},  # LIMPAR DO CHÃO
            14: {"tipo": "dias_uteis"},  # LIMPAR MOBÍLIA
        },
    },

    "06": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 31,
        "linha_responsavel_execucao": 32,
        "linha_responsavel_verificacao": 33,
        "linha_responsavel_supervisao": 34,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,
    },

    "07": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_uteis"},  # RETIRAR LIXO
            12: {"tipo": "dias_uteis"},  # LIMPEZA DA MOBÍLIA
            13: {"tipo": "dias_semana", "dias": [1, 3, 4]},  # TER, QUI, SEX
            14: {"tipo": "dias_uteis"},  # LIMPEZA DO CHÃO
            15: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            16: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            17: {"tipo": "dias_uteis"},  # LIMPEZA DA COPA
        },
    },

    "08": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_semana", "dias": [0, 2, 4]},  # SEG, QUA, SEX
            12: {"tipo": "dias_semana", "dias": [0, 2, 4]},
            13: {"tipo": "dias_semana", "dias": [0, 2, 4]},
            14: {"tipo": "dias_semana", "dias": [0, 2, 4]},
        },
    },

    "09": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_uteis"},
            12: {"tipo": "dias_uteis"},
            13: {"tipo": "dias_uteis"},
            14: {"tipo": "dias_uteis"},
            15: {"tipo": "dias_uteis"},
            16: {"tipo": "dias_uteis"},
            17: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            18: {"tipo": "dias_semana", "dias": [3]},  # QUINTA
            19: {"tipo": "dias_uteis"},
            20: {"tipo": "dias_uteis"},
            21: {"tipo": "dias_uteis"},
            22: {"tipo": "dias_uteis"},
        },
    },

    "10": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_semana", "dias": [1]},  # TERÇA
            12: {"tipo": "dias_semana", "dias": [1]},
            13: {"tipo": "dias_semana", "dias": [1]},
            14: {"tipo": "dias_semana", "dias": [1]},
            15: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            16: {"tipo": "dias_semana", "dias": [4]},
            17: {"tipo": "dias_semana", "dias": [2]},  # QUARTA
        },
    },

    "11": {
    "celula_mes_ano": "D7",
    "linha_numero_dia": 9,
    "linha_dia_semana": 10,
    "coluna_inicial_dias": 9,  # I

    "linha_inicio_preenchimento": 11,
    "linha_fim_preenchimento": 25,

    "linha_responsavel_execucao": 26,
    "linha_responsavel_verificacao": 27,
    "linha_responsavel_supervisao": 28,

    "altura_linha_execucao": 85,
    "altura_linha_verificacao": 85,
    "altura_linha_supervisao": 65,

    "regras_preenchimento": {
        11: {"tipo": "dias_uteis"},  # RETIRAR LIXO
        12: {"tipo": "dias_uteis"},  # LIMPEZA DA MOBÍLIA
        13: {"tipo": "dias_uteis"},  # LIMPEZA GERAL DOS ARMÁRIOS
        14: {"tipo": "dias_uteis"},  # LIMPEZA DO CHÃO
        15: {"tipo": "dias_uteis"},  # RETIRADA DE TEIA DE ARANHA
        16: {"tipo": "dias_uteis"},  # SHIRINK
    },
},

    "12": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_uteis"},
            12: {"tipo": "dias_uteis"},
            13: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            14: {"tipo": "dias_uteis"},
            15: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            16: {"tipo": "dias_uteis"},
        },
    },

    "13": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_uteis"},
            12: {"tipo": "dias_semana", "dias": [2]},  # QUARTA
            13: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            14: {"tipo": "dias_semana", "dias": [3]},  # QUINTA
            15: {"tipo": "dias_semana", "dias": [2, 4]},  # QUA, SEX
            16: {"tipo": "dias_semana", "dias": [0]},  # SEGUNDA
        },
    },

    "14": {
        "celula_mes_ano": "D7",
        "linha_numero_dia": 9,
        "linha_dia_semana": 10,
        "coluna_inicial_dias": 9,  # I
        "linha_inicio_preenchimento": 11,
        "linha_fim_preenchimento": 25,
        "linha_responsavel_execucao": 26,
        "linha_responsavel_verificacao": 27,
        "linha_responsavel_supervisao": 28,

        "altura_linha_execucao": 85,
        "altura_linha_verificacao": 85,
        "altura_linha_supervisao": 65,

        "regras_preenchimento": {
            11: {"tipo": "dias_semana", "dias": [1]},  # TERÇA
            12: {"tipo": "dias_semana", "dias": [2]},  # QUARTA
            13: {"tipo": "dias_semana", "dias": [0]},  # SEGUNDA
            14: {"tipo": "dias_semana", "dias": [4]},  # SEXTA
            15: {"tipo": "dias_semana", "dias": [1]},  # TERÇA
            16: {"tipo": "dias_semana", "dias": [3]},  # QUINTA
            17: {"tipo": "dias_semana", "dias": [0]},  # SEGUNDA
            18: {"tipo": "dias_semana", "dias": [2, 4]},  # QUA, SEX
        },
    },
}