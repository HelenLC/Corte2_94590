
class persona:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.frase=None

    def hablar(self):
        return self.frase
    #self:objeto



def main():
    estudiante = persona()
    estudiante.nombre='Helen'
    estudiante.apellido='Lopez'
    estudiante.edad=18
    estudiante.frase='Oh debo estudiar'

    futbolista = persona()
    futbolista.nombre='Radamel'
    futbolista.apellido='Garcia'
    futbolista.edad=36
    futbolista.frase='Goooooool'

    print(f'El estudiante dice: {estudiante.hablar()}')
    print(f'El señor futbolista dice: {futbolista.hablar()}')


if __name__=='__main__':
    main()