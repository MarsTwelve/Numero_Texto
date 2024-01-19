dict_unidades = {1: "um", 2: "dois", 3: "tres", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove",
                 10: "dez",
                 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis", 17: "dezessete",
                 18: "dezoito",
                 19: "dezenove"}

dict_dezenas = {1: "dez", 2: "vinte", 3: "trinta", 4: "quarenta", 5: "cinquenta", 6: "sessenta", 7: "setenta",
                8: "oitenta",
                9: "noventa"}

dict_centenas = {1: "cento", 2: "duzentos", 3: "trezentos", 4: "quatrocentos", 5: "quinhentos", 6: "seiscentos",
                 7: "setecentos", 8: "oitocentos", 9: "novecentos"}

numero_digitado = int(input("Digite um numero de ate tres casas: "))


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


if numero_digitado >= 20:
    if len(str(numero_digitado)) == 2:
        dezena = remove_dezena(numero_digitado)
        unidade = remove_unidade(numero_digitado)
        if unidade == 0:
            print(dict_dezenas[dezena])
        else:
            print(f"{dict_dezenas[dezena]} e {dict_unidades[unidade]}")

    if len(str(numero_digitado)) == 3:
        centena = remove_centena(numero_digitado)
        dezena = remove_dezena(numero_digitado)
        unidade = remove_unidade(numero_digitado)
        if dezena == 0 and unidade == 0:
            print("cem")
        elif dezena == 0:
            print(f"{dict_centenas[centena]} e {dict_unidades[unidade]}")
        elif unidade == 0:
            print(f"{dict_centenas[centena]} e {dict_dezenas[dezena]}")
        elif dezena == 1:
            print(f"{dict_centenas[centena]} e {dict_unidades[unidade + 10]}")
        else:
            print(f"{dict_centenas[centena]} e {dict_dezenas[dezena]} e {dict_unidades[unidade]}")
else:
    print(dict_unidades[numero_digitado])
