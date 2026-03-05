def fatorial(numero):
    valor = numero
    for _ in range(1, numero):
        valor *= numero - 1
        numero -= 1
    return valor

def ang_radiano(angulo):
    radiano = angulo * 3.1415 / 180
    return radiano

