# condigo que calcula la derivada de una exponecial
def derivada(base, exponente):
    base = exponente * base
    exponente = exponente - 1

    print(base, exponente)

# x^2
# 2x, si x = 4
# 2(4) = 8
derivada(4, 2) # esperamos un 8
