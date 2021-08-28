class Unidade_Federativa:

    def __init__(self, uf, uf_abreviacao, uf_lista_estados, uf_lista_uf):
        self.__uf = " " #santa catarina
        self.__uf_sigla = " " #SC
        self.__uf_lista_estados = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Espírito Santo"]
        self.__uf_lista_uf = ["AC", "AL", "AP", "AM", "BA", "CE", "ES"]

    def f_uf(self):
        return self.__uf
    def get_uf(self):
        self.__uf = self.__uf_lista_uf

    def f_uf_abreviacao(self):
        return self.__uf_abreviacao
    def get_uf_abraviacao(self):
        self.__uf_abreviacao = self.__uf_lista_estados

