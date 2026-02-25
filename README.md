# TRABAJO FINAL DE MÓDULO 3

### D O C T O R   P Y T H O N


##### Introducción
Este es un mini proyecto correspondiente a la evaluación final del Módulo 3 Fundamentos de Programación en Python, el cual consiste en crear un programa para registrar, ver, modificar, buscar y eliminar horas médicas.

Su funcionamiento es en base a funciones tanto predefinidas como definidas por usuario, además del uso de una lista para contener la información ingresada.


###### PROGRESO
__24/02:__ Estructura básica definida, principales funciones definidas (4/5)
__25/02:__ Funciones básicas terminadas. Se prueba nuevamente: agrega, modifica datos y elimina horas sin problemas. problema 1 persiste, otro detalle descubierto.
__25/02/2026:__ Funciones consolidadas y probadas. Funcionamiento al 100%. Recibe, agrega, modifica y elimina datos correctamente con mensajes respectivos.

###### COSAS A CORREGIR
~~- no se muestra mensaje en caso de no haber tanto horas registradas en lista como en búsquedas~~ SOLUCIONADO - se incluyó condicional ___if not lista_horas___  para que arroje mensaje correspondiente en caso de no haber datos coincidentes-
~~- al modifcar dato en particular no se muestra el nombre del dato a cambiar, sino que {dato_modif}. no afecta al proceso como tal en todo caso.~~ SOLUCIONADO - no se había incluído _f_ antes de string.
~~- no funciona función buscar_hora()~~ SOLUCIONADO -se incluye variable _cita_ para indicar existencia de cita médica con valor booleano y poder modificar estado para mostrar información en caso de existir cita en sistema. 

###### COSAS A IMPLEMENTAR EN EL FUTURO
- validación datos específicos: fecha, correo, hora, rut (asignar formato esperado)