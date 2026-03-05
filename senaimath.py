def calcular_e(termos):
    e = 0
    fatorial = 1

    for n in range(termos):
        if n > 0:
            fatorial *= n
        e += 1 / fatorial

    return e


print(calcular_e(15))