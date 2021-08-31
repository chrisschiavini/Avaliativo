class Unidade_Federativa:
    @staticmethod
    def get_lista_uf():
        v_estados_ufs = ["Acre * AC ","Amazonas * AM ","Amapá * AP ", "Pará * PA ", "Rondônia * RO ", "Roraima * RO ", "Tocantins * TO ","Alagoas  * AL ", "Bahia * BA ",
                         "Ceará * CE ", "Maranhão * MA ", "Paraíba * PB ", "Pernambuco * PE ", "Piauí * PI ", "Rio Grande do Norte * RN ", "Sergipe * SE ",
                        "Paraná * PR ", "Rio Grande do sul * RS ", "Santa Catarina * SC ", "Espirito Santo * ES ", "Minas Gerais * MG ", "Rio de Janeiro * RJ ",
                         "São Paulo * SP ", "Goiás * GO ", "Mato Grosso * MT ", "Mato Grosso do Sul * MS ", "Distrito Federal * DF"]
        return v_estados_ufs


    @staticmethod
    def get_UF(estado_sigla):
        if estado_sigla == "AC":
           return  "Acre "
        elif estado_sigla == "AL":
           return  "Alagoas "
        elif estado_sigla == "AM":
           return  "Amazonas "
        elif estado_sigla == "AP":
           return "Amapa"
        elif estado_sigla == "BA":
           return " Bahia"
        elif estado_sigla == "CE":
           return " Ceára"
        elif estado_sigla == "DF":
           return " Distrito Federal"
        elif estado_sigla == "ES":
           return " Espirito Santo"
        elif estado_sigla == "GO":
           return " Goias"
        elif estado_sigla == "MA":
           return " Maranhão"
        elif estado_sigla == "MG":
           return " Minas Gerais"
        elif estado_sigla == "MS":
           return " Mato Grosso do Sul"
        elif estado_sigla == "MT":
           return " Mato Grosso"
        elif estado_sigla == "PA":
           return " Para"
        elif estado_sigla == "PB":
           return " Paraiba"
        elif estado_sigla == "PE":
           return " Pernambuco"
        elif estado_sigla == "PI":
           return " Piaui"
        elif estado_sigla == "PR":
            return " Parana"
        elif estado_sigla == "RJ":
            return " Rio de Janeiro"
        elif estado_sigla == "RN":
            return " Rio Grande do Norte"
        elif estado_sigla == "RO":
            return " Rondonia"
        elif estado_sigla == "RR":
            return " Roraima"
        elif estado_sigla == "RS":
            return " Rio Grande do Sul"
        elif estado_sigla == "SC":
            return " Santa Catarina"
        elif estado_sigla == "SE":
            return " Sergipe"
        elif estado_sigla == "SP":
            return "São Paulo"
