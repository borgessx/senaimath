def fatorial(numero):
    if numero == 0:
        return 1

    valor = numero
    for _ in range(1, numero):
        valor *= numero - 1
        numero -= 1
    return valor

def ang_radiano(angulo):
    radiano = angulo * 3.1415 / 180
    return radiano

def cosseno(grau, termos):
    radiano = ang_radiano(grau)
    cosseno = 0
    
    for n in range(termos):
        sinal_formula = (-1)**n
        numerador = radiano**(2*n)
        denominador = fatorial(2*n)
        termos = sinal_formula * (numerador / denominador)
        cosseno += termos
    return cosseno

