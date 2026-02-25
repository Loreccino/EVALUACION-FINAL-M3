# EVALUACIÓN FINAL MÓDULO 3 - DOCTOR PYTHON
lista_horas = []  #lista vacía para ir agregándolas aquí

# PASO 1. DEFINIR FUNCIONES BÁSICAS
# registro_hora()
def registro_hora():
    print("\n- - - REGISTRO   DE   CITAS   MÉDICAS - - -")
    paciente = {   #  diccionario para contener datos de pacientes
        "run": input("Ingrese RUN: "),
        "nombre": input("Nombre Completo: "),
        "dirección": input("Dirección: "),
        "edad": input("Edad Paciente: "), 
        "comuna": input("Comuna de residencia: "),
        "número Celular": input("Celular:"),
        "correo": input("Correo (usuario@mail.xx): "),
        "previsión": input("Previsión (FONASA, ISAPRE, FF.AA, otra): "), 
        "fecha": input("Fecha de Cita Médica: "), 
        "hora": input("Horario de Cita: ")
    }
    lista_horas.append(paciente)  #.append() para agregar hora a lista
    print("Cita médica reservada con éxito. \n")
    
# buscar_hora()
def buscar_hora():
    run_buscar = input("Ingrese RUN a buscar: ")
    cita = False

    for paciente in lista_horas:
        if paciente["run"] == run_buscar:
            print("\n - - - LISTA   DE   CITAS   MÉDICAS - - -")
            for campo, valor in paciente.items():
                print(f"{campo}: {valor}")
                cita = True
                break
        else:
            print("No hay horas que mostrar.")

# lista de horas
def lista_citas():
    print("- - - - - LISTA   DE   HORAS - - - - -")
    for paciente in lista_horas:
        print(f"Paciente: {paciente["nombre"]} - RUN: {paciente["run"]} - Fecha: {paciente["fecha"]}, Hora: {paciente["hora"]}")
        if paciente == None:
            print("No hay citas médicas registradas")


# modificar_hora()
def modificar_hora():
    run_modif = input("Ingrese RUN de Paciente: ")
    for paciente in lista_horas:
        if paciente["run"] == run_modif:
            print("¿Desea modificar todos los datos o solo un o en específico?")
            print("1. Toda la información \n2. Dato en específico")
            op_cambiar = input("Escoja opción: ")
            if op_cambiar == "1":
                paciente["run"] = input("Ingrese RUN: ")
                paciente["nombre"] = input("Ingrese Nombre: ")               
                paciente["dirección"] = input("Ingrese Dirección: ")
                paciente["edad"] = input("Ingrese Edad: ")
                paciente["comuna"] = input("Ingrese Comuna: ")
                paciente["número celular"] = input("Ingrese Celular: ")
                paciente["correo"] = input("Ingrese Correo: ")
                paciente["previsión"] = input("Ingrese Previsión: ")
                paciente["fecha"] = input("Ingrese Fecha: ")
                paciente["hora"] = input("Ingrese Hora: ")

                print("\nDatos actualizados con éxito!")

            elif op_cambiar =="2":
                dato_modif = input("¿Qué dato desea modificar de la cita?: ")
                if dato_modif in paciente:
                    paciente[dato_modif] = input("{dato_modif}: ")
                    print("Dato actualizado con éxito!")
            else:
                print("Opción no válida. Intente nuevamente.")
        else:
            print("RUN no encontrado")

# eliminar_hora()
def eliminar_hora():
    print("- - - - - ELIMINAR   CITA   MÉDICA - - - - -")
    run_borrar = input("Ingrese RUN de Paciente: ")
    for i in range(len(lista_horas)):  #ciclo for para buscar RUN de paciente, i para indexar, len para contabilizar
        if lista_horas[i]["run"] == run_borrar:
            lista_horas.pop(i)   #  eliminar hora por indice
            print("Cita médica eliminada correctamente. \n")
        else:
            print("No hay citas médicas registradas para eliminar")


# PASO 2. MENU + INPUTS

def menu():
    while True:  # ejecutar el menú hasta que elija opción 5 (salir)
        print("=*" * 5, "D O C T O R   P Y T H O N ", "*=" * 5)
        print("Elija la acción a realizar: ")
        print("1. Registrar Hora Médica \n2. Lista de Citas Registradas\n" \
        "3. Buscar Horas Médicas \n" \
        "4. Modificar Datos Hora \n" \
        "5. Eliminar Reserva Hora \n" \
        "6. Salir")
        opcion = input("Ingrese opción: ")

    # 1. REGISTRAR HORA
        if opcion == "1":
            registro_hora()
    # 2. BUSCAR HORAS
        elif opcion == "2":
            lista_citas()
        elif opcion == "3":
            buscar_hora()
    # 3. MODIFICAR HORA
        elif opcion == "4":
            modificar_hora()
    # 4. ELIMINAR HORA
        elif opcion == "5":
            eliminar_hora()
    # 5. SALIR DEL PROGRAMA
        elif opcion == "6":
            print("\nC e r r a n d o   p r o g r a m a . . .")
            break  #  break para detener bucle y programa
        else:
            print("Opción no válida. Intente nuevamente.\n \n")


menu()