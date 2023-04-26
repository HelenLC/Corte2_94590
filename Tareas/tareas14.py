class personas:
    def __init__(self):
        self.__nombre=None
        self.__altura=None
        self.__peso=None

#-----------Getters----------- #recoger
    def getNombre(self):
        return self.__nombre 

    def getAltura(self):
        return self.__altura 

    def getPeso(self):
        return self.__peso

#-----------Setters----------- #modificar
    def setNombre(self,nombre :str):
        self.__nombre = nombre

    def setAltura(self,altura:int):
        self.__altura = altura

    def setPeso(self,peso :float):
        self.__peso =peso

#-----------Metodo IMC-----------

    def __Indice(self):
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
        
    def getIMC(self):
        return self.__Indice()

def main():
    entrada=[]
    for i in range(3):
        entrada.append(input('entrada: '))
    estudiante = personas()
    estudiante.setNombre(entrada[0])
    estudiante.setAltura(int(entrada[1]))
    estudiante.setPeso(float(entrada[2]))
    print(f'su IMC es: {estudiante.getIMC()}')

if __name__:"__main__"
main()
class personas:
    def __init__(self):
        self.__nombre=None
        self.__altura=None
        self.__peso=None

#-----------Getters----------- #recoger
    def getNombre(self):
        return self.__nombre 

    def getAltura(self):
        return self.__altura 

    def getPeso(self):
        return self.__peso

#-----------Setters----------- #modificar
    def setNombre(self,nombre :str):
        self.__nombre = nombre

    def setAltura(self,altura:int):
        self.__altura = altura

    def setPeso(self,peso :float):
        self.__peso =peso

#-----------Metodo IMC-----------

    def __Indice(self):
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
        
    def getIMC(self):
        return self.__Indice()

def main():
    entrada=[]
    for i in range(3):
        entrada.append(input('entrada: '))
    estudiante = personas()
    estudiante.setNombre(entrada[0])
    estudiante.setAltura(int(entrada[1]))
    estudiante.setPeso(float(entrada[2]))
    print(f'su IMC es: {estudiante.getIMC()}')

if __name__:"__main__"
main()