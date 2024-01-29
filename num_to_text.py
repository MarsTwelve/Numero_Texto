dict_unidades = {0: "zero", 1: "um", 2: "dois", 3: "tres", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove",
                 10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
                 17: "dezessete", 18: "dezoito", 19: "dezenove"}

dict_dezenas = {1: "dez", 2: "vinte", 3: "trinta", 4: "quarenta", 5: "cinquenta", 6: "sessenta", 7: "setenta",
                8: "oitenta", 9: "noventa"}

dict_centenas = {1: "cento", 2: "duzentos", 3: "trezentos", 4: "quatrocentos", 5: "quinhentos", 6: "seiscentos",
                 7: "setecentos", 8: "oitocentos", 9: "novecentos"}


def digitar_numero():
    numero_digitado = int(input("Digite um numero de ate tres casas: "))
    print(checagem(numero_digitado))
    escolher_opcao()


def remove_unidade(numero):
    unidade = numero % 10
    return unidade


def remove_dezena(numero):
    dezena = numero // 10
    if dezena >= 10:
        dezena = remove_unidade(dezena)
    return dezena


def remove_centena(numero):
    centena = numero // 100
    return centena


def checagem(numero_digitado):
    if numero_digitado < 20:
        return dict_unidades[numero_digitado]

    if len(str(numero_digitado)) == 2:
        dezena = remove_dezena(numero_digitado)
        unidade = remove_unidade(numero_digitado)
        dezena_extenso = dict_dezenas[dezena]
        if unidade != 0:
            return f"{dezena_extenso} e {dict_unidades[unidade]} "
        return dezena_extenso

    if len(str(numero_digitado)) == 3:
        centena = remove_centena(numero_digitado)
        dezena = remove_dezena(numero_digitado)
        unidade = remove_unidade(numero_digitado)

        centena_extenso = dict_centenas[centena]
        if dezena != 0 or unidade != 0:
            if dezena == 0:
                return f"{centena_extenso} e {dict_unidades[unidade]}"
            if unidade == 0:
                return f"{centena_extenso} e {dict_dezenas[dezena]}"
            if dezena == 1:
                return f"{centena_extenso} e {dict_unidades[unidade] + 10}"
            return f"{centena_extenso} e {dict_dezenas[dezena]} e {dict_unidades[unidade]}"
        if centena != 1:
            return centena_extenso
        return "cem"


def escolher_opcao():
    while True:
        opcao = input("deseja digitar um novo numero ? (Y/N)\n").upper()
        if opcao == "Y":
            digitar_numero()
            break
        if opcao == "N":
            break


digitar_numero()
