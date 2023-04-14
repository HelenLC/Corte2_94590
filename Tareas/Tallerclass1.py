def main():
    rta="si"
while 
rta=="si" or rta == "SI"

materias = ["Calculo", "Programacion", "Inglés", "Materiales", "Física"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
horas = ["07:00 - 09:00", "13:00 - 15:", "9:00 - 10:30", "11:00 - 13:00", "9:00 - 11:00"]
salones = ["DB-407", "GO-302", "DB-303", "DS-418", "PS-205"]
profesores = ["Oscar Mariño", "Nicolas torres", "Carlos Ruiz", "Hernan Pineda", "Paula Dorado"]

  # Solicitar al usuario el nombre de la materia para consultar su horario
print("Materias disponibles ",materias)
materia = input("Ingrese el nombre de la materia: ")

  # Verificar si la materia está en el horario y mostrar su información
if materia in materias:
      indice = materias.index(materia)
      print("Día de clase:", dias[indice])
      print("Hora de clase:", horas[indice])
      print("Salón de clase:", salones[indice])
      print("Profesor de la materia:", profesores[indice])
else:
      print("La materia no está en el horario.")

rta=input("¿Desea continuar con el programa?(si/no)")
 
else:

print("saliendo del sistema...")

if __name__=="__main__":
    main()
