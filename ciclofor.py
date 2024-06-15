#arreglos
numeros=[8,7,8,2,6,1,9,24,25]

for n in numeros:
    print(n)

#diccionarios
valores= {'A':3, 'E': 4, 'I': 5}

# for d in valores:
#     print(d)

for d in valores.values():
    print(d)

for d, v in valores.items():
    print(f'{d} : {v}')

for i in range(0,11,2):
    print(i)