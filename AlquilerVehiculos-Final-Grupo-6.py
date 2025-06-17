# TP Final - Alquiler de Vehículos
# Apellidos: Franco Martínez y Benjamín Martínez
# Comisión: 1

print("Seleccione la opción que coincida con usted:")
print("Elija 1, 2 ó 3 ")
print("")
print("1. Local")
print("2. Turista nacional")
print("3. Turista extranjero")
print("--------------------------------------------------")
print("")
print("Ingrese la opción: ")
ingreso_completo = False
while not ingreso_completo:
    try:
        origen = int(input())
        if origen in [1, 2, 3]:
            ingreso_completo = True
        else:
            print("Solo puede elejir 1, 2, o 3")
    except ValueError:
        print("Solo se pueden ingresar datos numéricos.")

print("--------------------------------------------------")
print("Ingrese su edad: ")
ingreso_completo = False
while not ingreso_completo:
    try:
        edad = int(input())
        if edad in range(1, 100):
            ingreso_completo = True
        else:
            print("Solo puede elejir un número entre 1 y 99")
    except ValueError:
        print("Solo se pueden ingresar datos numéricos.")

print("--------------------------------------------------")       
if edad >= 25:
    print("¿Posee una licencia válida para conducir? (1 = Sí, 2 = No)")
    print("En caso de ser turista extranjero:")
    print("¿Posee licencia internacional para turistas?")
    ingreso_completo = False
    while not ingreso_completo:
        try:
            tiene_licencia = int(input())
            if tiene_licencia in [1, 2]:
                ingreso_completo = True
            else:
                print("Solo puede elejir 1 o 2")
        except ValueError:
            print("Solo se pueden ingresar datos numéricos.")

    print("--------------------------------------------------")
    if tiene_licencia==1:
        print("Puede continuar con el proceso de alquiler.")
        if origen==3:
            print("Para registrarse ingrese su pasaporte:")
            ingreso_completo = False
            while not ingreso_completo:
                try:
                    pasaporte = int(input())
                    if pasaporte > 0:
                        ingreso_completo = True
                    else:
                        print("Ingrese su pasaporte sin signos")
                except ValueError:
                    print("Solo se pueden ingresar datos numéricos.")
        else:
            print("--------------------------------------------------")
            print("Ingrese su DNI: ")
            ingreso_completo = False
            while not ingreso_completo:
                try:
                    dni = int(input())
                    if dni > 0:
                        ingreso_completo = True
                    else:
                        print("Ingrese su DNI sin signos")
                except ValueError:
                    print("Solo se pueden ingresar datos numéricos.")

        print("Ingrese su nombre:")
        nombre = input()
        print("Ingrese su apellido:")
        apellido = input()
        print("Ingrese su teléfono:")
        telefono = input()
        print("Ingrese su domicilio:")
        domicilio = input()
        print("Ingrese el nombre de la empresa en la que trabaja:")
        empresa = input()
        print("Ingrese los teléfonos laborales:")
        ingreso_completo = False
        while not ingreso_completo:
            try:
                telefonos_laborales = int(input())
                if origen >0:
                    ingreso_completo = True
                else:
                    print("Ingrese su número sin signos")
            except ValueError:
                print("Solo se pueden ingresar datos numéricos.")

        print("--------------------------------------------------")
        print("Ingrese su domicilio laboral:")
        domicilio_laboral = input()

        print("--------------------------------------------------")
        print("¿Es cliente VIP?")
        print("Elija 1 o 2 ")
        print("1. Sí")
        print("2. No")
        ingreso_completo = False
        while not ingreso_completo:
            try:
                vip = int(input())
                if vip in [1, 2]:
                    ingreso_completo = True
                else:
                    print("Solo puede elejir 1, o 2")
            except ValueError:
                print("Solo se pueden ingresar datos numéricos.")
        
        print("--------------------------------------------------")
        if vip==1:
            print("Ingrese la ID de su tarjeta VIP (xxxx):")
            ingreso_completo = False
            while not ingreso_completo:
                try:
                    id_vip = int(input())
                    if id_vip in range(1000, 9999):
                        ingreso_completo = True
                    else:
                        print("Solo puede ingresar 4 digitos sin signos")
                except ValueError:
                    print("Solo se pueden ingresar datos numéricos.")

        else:
            print("--------------------------------------------------")
            print("Seleccione la forma de pago:")
            print("1. Efectivo")
            print("2. Tarjeta de crédito")
            print("3. Tarjeta de débito")
            print("4. Transferencia bancaria")
            print("--------------------------------------------------")
            ingreso_completo = False
            while not ingreso_completo:
                try:
                    forma_pago = int(input())
                    if forma_pago in [1, 2, 3, 4]:
                        ingreso_completo = True
                    else:
                        print("Solo puede elejir 1, 2, 3 o 4")
                except ValueError:
                    print("Solo se pueden ingresar datos numéricos.")

            print("--------------------------------------------------")
            print("¿Cómo conoció la agencia?")
            print("1. Recomendación")
            print("2. Redes sociales")
            print("3. Búsqueda en Internet")
            print("4. Publicidad en la calle")
            print("--------------------------------------------------")
            ingreso_completo = False
            while not ingreso_completo:
                try:
                    conoce_agencia = int(input())
                    if conoce_agencia in [1, 2, 3, 4]:
                        ingreso_completo = True
                    else:
                        print("Solo puede elejir 1, 2, 3 o 4")
                except ValueError:
                    print("Solo se pueden ingresar datos numéricos.")

        print("--------------------------------------------------")
        print("¿El vehículo se utilizará en la zona de Bariloche? (1 = Sí, 2 = No)")
        ingreso_completo = False
        while not ingreso_completo:
            try:
                en_bariloche = int(input())
                if en_bariloche in [1, 2]:
                    ingreso_completo = True
                else:
                    print("Solo puede elejir 1, o 2")
            except ValueError:
                print("Solo se pueden ingresar datos numéricos.")

        print("--------------------------------------------------")
        if en_bariloche==1:
            print("IMPORTANTE: Para zonas de terreno montañoso o ripio, el vehículo debe ser 4x4 con equipamiento de invierno obligatoriamente.")
            print("¿Recorrerá zonas de terreno montañoso o ripio? (1 = Sí, 2 = No)")
            ingreso_completo = False
            while not ingreso_completo:
                try:
                    tipo_terreno = int(input())
                    if tipo_terreno in [1, 2]:
                        ingreso_completo = True
                    else:
                        print("Solo puede elejir 1, o 2")
                except ValueError:
                    print("Solo se pueden ingresar datos numéricos.")

            print("--------------------------------------------------")
            if tipo_terreno==1:
                tipo_vehiculo = "4x4"
                equip_invierno = "Sí"
            else:
                print("Seleccione el tipo de vehículo que desea alquilar:")
                print("1. Auto")
                print("2. Camioneta")
                ingreso_completo = False
                while not ingreso_completo:
                    try:
                        opcion_vehiculo = int(input())
                        if opcion_vehiculo in [1, 2]:
                            ingreso_completo = True
                        else:
                            print("Solo puede elejir 1, o 2")
                    except ValueError:
                        print("Solo se pueden ingresar datos numéricos.")

                print("--------------------------------------------------")
                if opcion_vehiculo==1:
                    tipo_vehiculo = "Auto"
                else:
                    tipo_vehiculo = "Camioneta"
                print("¿Desea equipamiento de invierno? (1 = Sí, 2 = No)")
                ingreso_completo = False
                while not ingreso_completo:
                    try:
                        equip_invierno = int(input())
                        if equip_invierno in [1, 2]:
                            ingreso_completo = True
                        else:
                            print("Solo puede elejir 1, o 2")
                    except ValueError:
                        print("Solo se pueden ingresar datos numéricos.")

        else:
            print("--------------------------------------------------")
            print("Seleccione el tipo de vehículo que desea alquilar:")
            print("1. Auto")
            print("2. Camioneta")
            ingreso_completo = False
            while not ingreso_completo:
                try:
                    opcion_vehiculo = int(input())
                    if opcion_vehiculo in [1, 2]:
                        ingreso_completo = True
                    else:
                        print("Solo puede elejir 1, o 2")
                except ValueError:
                    print("Solo se pueden ingresar datos numéricos.")

            if opcion_vehiculo==1:
                tipo_vehiculo = "Auto"
            else:
                tipo_vehiculo = "Camioneta"

        print("--------------------------------------------------")
        print("Seleccione el tipo de tarifa:")
        print("1. Diaria")
        print("2. Fin de semana")
        print("3. Semana")
        print("4. Mes o más")
        ingreso_completo = False
        while not ingreso_completo:
            try:
                tipo_tarifa = int(input())
                if tipo_tarifa in [1, 2, 3, 4]:
                    ingreso_completo = True
                else:
                    print("Solo puede elejir 1, 2, 3 o 4")
            except ValueError:
                print("Solo se pueden ingresar datos numéricos.")

        print("--------------------------------------------------")
        print("Es temporada alta?:")
        print("1. si")
        print("2. no")
        ingreso_completo = False
        while not ingreso_completo:
            try:
                temporada_alta = int(input())
                if temporada_alta in [1, 2]:
                    ingreso_completo = True
                else:
                    print("Solo puede elejir 1, o 2")
            except ValueError:
                print("Solo se pueden ingresar datos numéricos.")
        
        print("--------------------------------------------------")
        total_seguros = 0
        print("Se ha incluido el seguro obligatorio de la Comisión Nacinal de Seguro.")
        print("Importe: $5000")
        total_seguros = total_seguros+5000

        print("--------------------------------------------------")
        if tipo_terreno==1:
            print("Se ha incluido seguro adicional por terreno montañoso o ripio")
            total_seguros = total_seguros+3000

        importe_veh = 0
        if tipo_vehiculo=="Auto":
            importe_veh = 10000
        if tipo_vehiculo=="Camioneta":
            importe_veh = 15000
        if tipo_vehiculo=="4x4":
            importe_veh = 20000
        recargo_temp = 0
        if temporada_alta==1:
            recargo_temp = importe_veh*0.10
        subtotal = importe_veh + recargo_temp
        descuento_vip = 0
        if vip==1:
            descuento_vip = subtotal*0.15
        total_final = subtotal-descuento_vip+total_seguros

        print("")
        print("------------- FACTURA -------------")
        print("Cliente: ",nombre," ",apellido)
        if origen==3:
            print("Pasaporte: ",pasaporte)
        else:
            print("DNI: ",dni)
        print("Tipo de vehículo: ",tipo_vehiculo)
        print("Equipamiento de invierno: ",equip_invierno)
        print("Tarifa: ",tipo_tarifa)
        print("-----------------------------------")
        print("Importe del vehículo: $",importe_veh)
        print("Recargo por temporada alta: $",recargo_temp)
        print("Descuento VIP: -$",descuento_vip)
        print("Total seguros: $",total_seguros)
        print("-----------------------------------")
        print("TOTAL A PAGAR: $",total_final)
        print("-----------------------------------")
        print("El encargado de playa ha registrado la devolución del vehículo.")
        print("La factura fue enviada al cliente y archivada en el sistema.")
        print("-----------------------------------")
    else:
        print(("Tiene que tener licencia"))
else:
    print(("Tiene que ser mayor de 25 años"))
