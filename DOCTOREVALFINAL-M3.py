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
    lista_horas.append(paciente)
    print("Cita médica reservada con éxito")
# buscar_hora()
def buscar_hora():
    pass
# modificar_hora()
def modificar_hora():
    pass
# eliminar_hora()
def eliminar_hora():
    pass
# * en TODAS se busca con RUT

# PASO 2. MENU + INPUTS

def menu():
    while True:  # ejecutar el menú hasta que elija opción 5 (salir)
        print("=*" * 5, "D O C T O R   P Y T H O N ", "*=" * 5)
        print("Elija la acción a realizar: ")
        print("1. Registrar Hora Médica \n" \
        "2. Buscar Horas Médicas \n" \
        "3. Modificar Datos Hora \n" \
        "4. Eliminar Reserva Hora \n" \
        "5. Salir")
        opcion = input("Ingrese opción: ")

    # 1. REGISTRAR HORA
        if opcion == "1":
            registro_hora()
    # 2. BUSCAR HORAS
        elif opcion == "2":
            buscar_hora()
    # 3. MODIFICAR HORA
        elif opcion == "3":
            modificar_hora()
    # 4. ELIMINAR HORA
        elif opcion == "4":
            eliminar_hora()
    # 5. SALIR DEL PROGRAMA
        elif opcion == "5":
            print("\nC e r r a n d o   p r o g r a m a . . .")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n \n")


menu()