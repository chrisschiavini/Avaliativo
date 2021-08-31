from Estados import Unidade_Federativa

estado_sigla = input('Digite a sigla do estado ')

if estado_sigla != '':
    uf = Unidade_Federativa.get_UF(estado_sigla)
    print("a UF da sigla " + str(estado_sigla) + " é " + str(uf))
else:
    print("Unidades Federativas Brasileiras")

if estado_sigla == '':

    unidades_federativas = Unidade_Federativa.get_lista_uf()

    for counter, value in enumerate(unidades_federativas):
        print(value)
else:
    print("Obrigado por utilizar nosso sistema")

