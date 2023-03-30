
class personas:
    def __init__(self):
        self.nombre=None
        self.altura=None
        self.peso=None

    def Indice(self):
        IMC=self.peso/((self.altura/100)**2)
        if IMC<= 18.5:
            return str('Por debajo')
        elif IMC <=24.9:
            return str('Saludable')
        elif IMC <=29.9:
            return str('Sobrepeso')
        elif IMC <=34.9:
            return str('Obesidad 1')
        elif IMC <=39.9:
            return str('Obesidad 2')
        else:
            return str('Obesidad 3')

def main():
    estudiante1 = personas()
    estudiante1.nombre='Pedro Caceres'
    estudiante1.altura=188
    estudiante1.peso=97

    estudiante2 = personas()
    estudiante2.nombre='Maria Perez'
    estudiante2.altura=160
    estudiante2.peso=47

    estudiante3 = personas()
    estudiante3.nombre='Julian Dominguez'
    estudiante3.altura=158
    estudiante3.peso=58

    estudiante4 = personas()
    estudiante4.nombre='Jessica Fuentes'
    estudiante4.altura=170
    estudiante4.peso=73

    print(f'estudiante: {estudiante1.nombre} resultado: {estudiante1.Indice()}')
    print(f'estudiante: {estudiante2.nombre} resultado: {estudiante2.Indice()}')
    print(f'estudiante: {estudiante3.nombre} resultado: {estudiante3.Indice()}')
    print(f'estudiante: {estudiante4.nombre} resultado: {estudiante4.Indice()}')

if __name__:"__main__"
main()