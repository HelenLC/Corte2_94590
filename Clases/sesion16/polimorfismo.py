class Ciudadano():
    def __init__(self):
        self.__nombre =None
        self.__idioma =None

    #---------------Getters-----------
    def getNombre(self):
        return self.__nombre

    def getIdioma(self):
        return self.__idioma

    #-----------Setters--------
    def setNombre(self, nombre:str):
        self.__nombre=nombre

    def setIdioma(self, idioma:str):
        self._idioma=idioma

    #---------sobrecarga-----
    def saludo(self):
        return "Quoi de beau!"

class Colombia(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__CC=None
    
    def setCC(self, CC:int):
        self.__CC=CC

    def getCC(self):
        return self.__CC 

#---------sobrecarga-----
def saludo(self):
    return "Quiubo parce!"

class Inglaterra(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__id=None
    
    def setid(self, id:int):
        self.__id=id

    def getid(self):
        return self.__id 

#---------sobrecarga-----
def saludo(self):
    return "Hello my friend!"

class China(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__shengfenzheng=None
    
    def setshengfenzheng(self, shengfenzheng:int):
        self.__shengfenzheng=shengfenzheng   

    def getshengfenzheng(self):
        return self.__shengfenzheng

#---------sobrecarga-----
def saludo(self):
    return "NiGanMaYa!"

def darsaludo(obj):
    print(obj.saludo())

def main():
    colombiano=Colombia()
    colombiano.setNombre('Kevin')
    colombiano.setIdioma('español')
    colombiano.setCC(21589647)

    ingles=Inglaterra()
    ingles.setNombre('Richard')
    ingles.setIdioma('english')
    ingles.setid(49883229)

    chino=China()
    chino.setNombre('Liu')
    chino.setIdioma('mandarin')
    chino.setshengfenzheng(754945479764)

    ciudadano1=Ciudadano()
    ciudadano1.setNombre('karla')
    ciudadano1.setIdioma('frances')

    #---aplicantes-----------
    print(f'Aplicante: {colombiano.getNombre()}\n'+\
        f'Idioma: {colombiano.getIdioma()}\n' + \
            f'CC: {colombiano.getCC()}\n'+
            darsaludo(colombiano)+'\n')
    
    print(f'Aplicante: {ingles.getNombre()}\n'+\
        f'Idioma: {ingles.getIdioma()}\n' + \
            f'Id: {ingles.getId()}\n'+
            darsaludo(ingles)+'\n')
    
    print(f'Aplicante: {chino.getNombre()}\n'+\
        f'Idioma: {chino.getIdioma()}\n' + \
            f'getShengfenzheng: {chino.getShengfenzheng()}\n'+
            darsaludo(chino)+'\n')
    
    print(f'Aplicante: {ciudadano1.getNombre()}\n' + \
        f'Idioma: {ciudadano1.getIdioma()}\n'+\
            darsaludo(ciudadano1))

if __name__ == "__main__":
    main()