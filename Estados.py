class Unidade_Federativa:
@staticmethod
    def __init__(self, lista_uf,sigla_uf):
        self.lista_uf = lista_uf
        self.lista_uf = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ',
       'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
        self.sigla_uf = sigla_uf
        self.sigla_uf =['Acre', 'Alagoas', 'Amazonas', 'Amapá', 'Bahia', 'Ceará', 'Distrito Federal',
                        'Espirito Santo', 'Goiás', 'Maranão', 'Minas Gerais', 'Mato Grosso do Sul',
                        'Mato Grosso', 'Pará', 'Paraiba', 'Pernanbuco', 'Piaui', 'Paraná',
                        'Rio de Janeiro', 'Rio Grande do Norte', 'Rondonia', 'Roraima',
                        'Rio Grande do Sul', 'Santa Catarina', 'Sergipe',  'São Paulo',   'Tocantis']

estado = input("Digite sua UF: ")
Sigla = estado
if (estado == 'AC'):
    print("Seu estado é Acre")
elif (estado == 'AL'):
    print("Seu estado é Alagoas")
elif (estado == 'AM'):
    print("Seu estado é Amazonas")
elif (estado == 'AP'):
    print("Seu estado é Amapa")
elif (estado == 'BA'):
    print("Seu estado é Bahia")
elif (estado == 'CE'):
    print("Seu estado é Ceára")
elif (estado == 'DF'):
    print("Seu estado é Distrito Federal")
elif (estado == 'ES'):
    print("Seu estado é Espirito Santo")
elif (estado == 'GO'):
    print("Seu estado é Goias")
elif (estado == 'MA'):
    print("Seu estado é Maranhão")
elif (estado == 'MG'):
    print("Seu estado é Minas Gerais")
elif (estado == 'MS'):
    print("Seu estado é Mato Grosso do Sul")
elif (estado == 'MT'):
    print("Seu estado é Mato Grosso")
elif (estado == 'PA'):
    print("Seu estado é Para")
elif (estado == 'PB'):
    print("Seu estado é Paraiba")
elif (estado == 'PE'):
    print("Seu estado é Pernambuco")
elif (estado == 'PI'):
    print("Seu estado é Piaui")
elif (estado == 'PR'):
    print("Seu estado é Parana")
elif (estado == 'RJ'):
    print("Seu estado é Rio de Janeiro")
elif (estado == 'RN'):
    print("Seu estado é Rio Grande do Norte")
elif (estado == 'RO'):
    print("Seu estado é Rondonia")
elif (estado == 'RR'):
    print("Seu estado é Roraima")
elif (estado == 'RS'):
    print("Seu estado é Rio Grande do Sul")
elif (estado == 'SC'):
    print("Seu estado é Santa Catarina")
elif (estado == 'SE'):
    print("Seu estado é Sergipe")
elif (estado == 'SP'):
    print("Seu estado é São Paulo")
else:
    print("Seu Estado é inválido")
