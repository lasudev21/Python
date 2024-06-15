def multiplicacion(a, b):
    print(f'La multplicación es {a*b}')
    print(f'Y el resultado de esa multiplicacion es {par(b)}')


def par(a):
    if a % 2 == 0:
        return "Par"
    else:
        return "Impar"

multiplicacion(4,2)

# print(f'El numero es {par(3)}')