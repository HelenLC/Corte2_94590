import busqueda
def matriz(fila,columna):
    excel = {}
    f=open('organization_data.cvs','r')
    matriz = f.readlines()
    f.seek(0)
    for i in range(fila):
        matriz.append([])
        datos={'Index','Organization Id','Name','Website','Country','Description','Founded','Industry','Number of employees'}
    for j in range(columna):
        pos = str(f'{i}{j}')
        excel[pos] = datos[j]

def main():
    paises= open("organization_data.cvs","r")
    paises= paises.read().splitlines()
    paises_ordenar=sorted(paises)
    print(paises_ordenar)

    datos= open('organization_data.cvs', 'r')
    datos = datos.read().splitlines()
    datos_ordenar=sorted(datos)
    print(datos_ordenar)

    mayorempleado= open('organization_data.cvs', 'r')
    mayorempleado = mayorempleado.read().splitlines()
    mayorempleado_ordenar=sorted(mayorempleado)
    print(mayorempleado_ordenar)

    manorempleado= open('organization_data.cvs', 'r')
    manorempleado = manorempleado.read().splitlines()
    manorempleado_ordenar=sorted(manorempleado)
    print(manorempleado_ordenar)

    promedio= open('organization_data.cvs', 'r')
    promedio = promedio.read().splitlines()
    promedio_ordenar=sorted(promedio)
    print(promedio_ordenar)

    empresapais= open('organization_data.cvs', 'r')
    empresapais = empresapais.read().splitlines()
    empresapais=sorted(empresapais)
    print(empresapais)

    print(excel)
    f.close()

    busqueda.busqueda_excel(excel)





if __name__=="__main__":
    main()
