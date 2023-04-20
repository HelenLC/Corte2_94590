def lectura():
    n = open('organization_data.csv','rt')
    data = []
    linea = n.readline()
    while linea != ' ':
        data.append(linea.rstrip('\n').split(','))
        linea= n.readline()
    n.close()
    return data

def orden_paises(data):
    paises=[]
    for i in data[1:]:
        country=i[4]
        if country not in paises:
             paises.append(country)
    paises.sort()
    print(paises)
    return paises

def busqueda(data,paises):
    search=int(input('ingrese el indice de una pais'))
    compañias= []
    empleados= []
    for i in data:
        if i[4] == paises[search-1]:
            compañias.append(i)
            empleados.append(int(i[8]))
    return compañias, empleados

def imprimir(compañias, empleados):
    print(f'pais: {compañias[0][4]}\n')
    mayor=empleados.index(max(empleados))

    print(f'Empresa con mayor # de empleados:')
    rotulo=['Empresa:','Website:','Descripcion:','Fundacion:','Industria:','Empleados:']

    # print(compañias[mayor])
    # compañias.pop(4)
    # for i in range(len(rotulo)):
    #     if i !=4:
    #         print(f'{rotulo[i]} {compañias[mayor][i+2]}')


    print(f'Empresa: {compañias[mayor][2]}')
    print(f'Website: {compañias[mayor][3]}')
    print(f'Descripcion: {compañias[mayor][5]}')
    print(f'Fundacion: {compañias[mayor][6]}')
    print(f'Industria: {compañias[mayor][7]}')
    print(f'Empleados: {compañias[mayor][8]}')

    print(f'Empresa: {compañias[mayor][2]}')
    print(f'Website: {compañias[mayor][3]}')
    print(f'Descripcion: {compañias[mayor][5]}')
    print(f'Fundacion: {compañias[mayor][6]}')
    print(f'Industria: {compañias[mayor][7]}')
    print(f'Empleados: {compañias[mayor][8]}')

    print(mayor)
    print(compañias[mayor])


    print(f'Empresa con mayor # de empleados:')


def main():
    data=lectura()
    paises=orden_paises(data)
    data_compañias,data_empleados,busqueda(data, paises)
    imprimir(data_compañias, data_empleados)



if __name__=='__main__':
    main()