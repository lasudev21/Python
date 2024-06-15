class Coche:
    # Atributos
    reuda = 4
    color = ""
    aceleracion = 0
    velocidad = 0

    # Constructor
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    # Metodos
    # def acelerar(self):
    #     self.velocidad += self.aceleracion
    #     return self.velocidad
    
    def acelerar(self, velocidad = 0):
        if velocidad > 0:
            self.velocidad += velocidad
        else:
            self.velocidad += self.aceleracion
            
        return self.velocidad
    
class AutoVolador(Coche):
    ruedas = 6

    def __init__(self, color, aceleracion, estaVolando = False):
        super().__init__(color, aceleracion)
        self.estaVolando = estaVolando

    def vuela(self):
        self.estaVolando = True
        return 'Estoy volando'


c1 = Coche('Rojo', 10)

print(c1.color)
# print(c1.acelerar())
# print(c1.acelerar(50))

print('------------------------')
cv1 = AutoVolador('Negro', 60)
print(cv1.color)
print(cv1.estaVolando)
print(cv1.vuela())
print(cv1.estaVolando)