#----------clase padre----------
class Deportistas:
    def __init__(self,nombre:str,documento:int,edad:int, palmares:int):
       self.__nombre=nombre
       self.__documento=documento
       self.__edad=edad

#-------------Getters--------
    def getNombre(self):
       return self.__nombre

    def getDocumento(self):
        return self.__documento

    def getEdad(self):
       return self.__edad
    
#---------Setters-----
    def setNombre(self,nombre:str):
     self.__nombre=nombre

    def setdocumento(self,documento:int):
     self.__documento=documento

    def setEdad(self,edad:int):
     self.__edad=edad 

#-----------Sobrecarga metodo----------
def palmares(self):
   print('Ha ganado una medalla')

#-------------clase hijo----------
class Deportistafutbol(Deportistas):
   def __init__(self,nombre:str,documento:int, edad:int,golesanotados:int,nombreequipo:str):
        super().__init__(nombre,documento,edad)
        self.__golesanotados=golesanotados
        self.__nombreequipo=nombreequipo
   
   #--------Getters hijo----------
   def getgolesanotados(self,golesanotado:int): 
      return self.__golesanotados
   
   def getnombreequipo(self,nombreequipo:str):
      return self.__nombreequipo

def main():
   futbolista=Deportistafutbol('Falcaco',24152637,36, 35, 'Seleccion Colombia')

   print(f'Deportista:{futbolista.getNombre()}\n'+\
         f'documento:{futbolista.getDocumento()}\n'+\
        f'edad:{futbolista.getEdad()}\n'+\
        f'cantidad de goles:{futbolista.getgolesanotados()}\n+'\
        f'equipo:{futbolista.getnombreequipo()}\n+'\
        f'palmares:{futbolista.palmares()}')


if __name__=="__main__":
   main()
