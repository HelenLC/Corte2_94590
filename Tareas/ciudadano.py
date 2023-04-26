class Ciudadano():
    def __init__(self,nombre:str, edad:int, cc:int):
        self._nombre=nombre
        self._edad=edad
        self._cc=cc

    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad
    def get_cc(self):
        return self._cc 
    
    def set_nombre(self, nombre:str):
        self._nombre=nombre 

    def set_edad(self, edad:int):
        if edad<1:
            self._edad='Es un bebe con meses de nacido'
        else: 
            self._edad=edad
    def set_cc(self, cc:int):
        if 30>cc:
            self._cc= 'La cc debe ser de 10 digitos'
        else: 
            self._cc=cc     

    def _informacion(self):
        return print(f'nombre{self._nombre}, edad{self._edad}, cc{self._cc}')
    
    def _mayoredad(self):
        if self._edad>18:
            return print(f'Es mayor de edad')
        elif self._edad<18:
            return print(f'Es mejor de edad')
        else:
            return print(f'informacion{self._informacion}, mayoredad {self._mayoredad}')
        
    def main():
            persona=Ciudadano('Helen', 19, 1121706388)
            persona.set_nombre('Helen')
            persona.set_edad(19)
            persona.set_cc(1121706388)
            persona.getinformacion()
            persona.getmayoredad()

    if __name__=='__main__':
        main()