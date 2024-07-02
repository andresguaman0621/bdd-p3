from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

uri="mongodb://localhost:27017/"

# Conectar a MongoDB
client = MongoClient(uri)
db = client['SacramentosParroquias']

# citas = db.certificados.find()
# for cita in citas:
#   print(cita)



def mostrar_menu_principal():
    print("\n-- Menú Principal --")
    print("1. Consultas")
    print("2. Ingreso de información")
    print("3. Actualización de información")
    print("4. Eliminación de información")
    print("5. Salir")

def mostrar_submenu_consultas():
    print("\n-- Consultas --")
    print("1. Listar catequizandos por nivel")
    print("2. Buscar certificados de un catequizando")
    print("3. Ver inscripciones pendientes de pago")
    print("4. Listar catequistas por parroquia")
    print("5. Ver sacramentos realizados en un rango de fechas")
    print("6. Volver al menú principal")

def mostrar_submenu_ingresos():
    print("\n-- Ingreso de información --")
    print("1. Registrar nuevo catequizando")
    print("2. Añadir nueva inscripción")
    print("3. Registrar nuevo certificado")
    print("4. Añadir nuevo catequista")
    print("5. Volver al menú principal")

def mostrar_submenu_actualizaciones():
    print("\n-- Actualización de información --")
    print("1. Actualizar estado de pago de inscripción")
    print("2. Cambiar nivel de catecismo de un catequizando")
    print("3. Actualizar información de contacto de catequista")
    print("4. Modificar fecha de sacramento")
    print("5. Volver al menú principal")

def mostrar_submenu_eliminaciones():
    print("\n-- Eliminación de información --")
    print("1. Eliminar inscripción")
    print("2. Eliminar catequizando")
    print("3. Eliminar certificado")
    print("4. Eliminar catequista")
    print("5. Volver al menú principal")


# # Funciones de consulta
# def listar_catequizandos_por_nivel():
#     nivel = input("Ingrese el nivel de catecismo: ")
#     catequizandos = db.catequizandos.find({"nivel_actual": nivel})
#     for c in catequizandos:
#         print(f"{c['nombres']} {c['apellidos']} - ID: {c['_id']}")

# def buscar_certificados_catequizando():
#     id_catequizando = int(input("Ingrese el ID del catequizando: "))
#     certificados = db.certificados.find({"catequizando_id": id_catequizando})
#     for cert in certificados:
#         print(f"Nivel: {cert['nivel_catecismo']}, Fecha: {cert['fecha_emision']}")

# def ver_inscripciones_pendientes():
#     inscripciones = db.inscripciones.find({"pago_realizado": False})
#     for insc in inscripciones:
#         catequizando = db.catequizandos.find_one({"_id": insc['catequizando_id']})
#         print(f"{catequizando['nombres']} {catequizando['apellidos']} - Nivel: {insc['nivel_catecismo']}")

# def listar_catequistas_por_parroquia():
#     id_parroquia = int(input("Ingrese el ID de la parroquia: "))
#     catequistas = db.catequistas.find({"parroquia_id": id_parroquia})
#     for cat in catequistas:
#         print(f"{cat['nombres']} {cat['apellidos']} - Nivel: {cat['nivel_catecismo']}")

# def ver_sacramentos_por_fecha():
#     fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
#     fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
#     sacramentos = db.sacramentos.find({
#         "fecha": {
#             "$gte": datetime.strptime(fecha_inicio, "%Y-%m-%d"),
#             "$lte": datetime.strptime(fecha_fin, "%Y-%m-%d")
#         }
#     })
#     for sac in sacramentos:
#         print(f"Sacramento: {sac['nombre']}, Fecha: {sac['fecha']}")

# # Funciones de ingreso
# def registrar_catequizando():
#     catequizando = {
#         "nombres": input("Nombres: "),
#         "apellidos": input("Apellidos: "),
#         "fecha_nacimiento": datetime.strptime(input("Fecha de nacimiento (YYYY-MM-DD): "), "%Y-%m-%d"),
#         "nivel_actual": input("Nivel actual: "),
#         "parroquia_id": int(input("ID de la parroquia: "))
#     }
#     resultado = db.catequizandos.insert_one(catequizando)
#     print(f"Catequizando registrado con ID: {resultado.inserted_id}")

# def anadir_inscripcion():
#     inscripcion = {
#         "catequizando_id": int(input("ID del catequizando: ")),
#         "nivel_catecismo": input("Nivel de catecismo: "),
#         "fecha_inscripcion": datetime.now(),
#         "parroquia_id": int(input("ID de la parroquia: ")),
#         "pago_realizado": input("¿Pago realizado? (s/n): ").lower() == 's'
#     }
#     resultado = db.inscripciones.insert_one(inscripcion)
#     print(f"Inscripción registrada con ID: {resultado.inserted_id}")

# def registrar_certificado():
#     certificado = {
#         "catequizando_id": int(input("ID del catequizando: ")),
#         "nivel_catecismo": input("Nivel de catecismo: "),
#         "fecha_emision": datetime.now(),
#         "parroquia_id": int(input("ID de la parroquia: "))
#     }
#     resultado = db.certificados.insert_one(certificado)
#     print(f"Certificado registrado con ID: {resultado.inserted_id}")

# def anadir_catequista():
#     catequista = {
#         "nombres": input("Nombres: "),
#         "apellidos": input("Apellidos: "),
#         "parroquia_id": int(input("ID de la parroquia: ")),
#         "nivel_catecismo": input("Nivel de catecismo que imparte: ")
#     }
#     resultado = db.catequistas.insert_one(catequista)
#     print(f"Catequista registrado con ID: {resultado.inserted_id}")

# # Funciones de actualización
# def actualizar_pago_inscripcion():
#     id_inscripcion = int(input("ID de la inscripción: "))
#     nuevo_estado = input("¿Pago realizado? (s/n): ").lower() == 's'
#     db.inscripciones.update_one(
#         {"_id": id_inscripcion},
#         {"$set": {"pago_realizado": nuevo_estado}}
#     )
#     print("Estado de pago actualizado.")

# def cambiar_nivel_catequizando():
#     id_catequizando = int(input("ID del catequizando: "))
#     nuevo_nivel = input("Nuevo nivel: ")
#     db.catequizandos.update_one(
#         {"_id": id_catequizando},
#         {"$set": {"nivel_actual": nuevo_nivel}}
#     )
#     print("Nivel de catequizando actualizado.")

# def actualizar_contacto_catequista():
#     id_catequista = int(input("ID del catequista: "))
#     nuevo_telefono = input("Nuevo número de teléfono: ")
#     db.catequistas.update_one(
#         {"_id": id_catequista},
#         {"$set": {"telefono": nuevo_telefono}}
#     )
#     print("Información de contacto actualizada.")

# def modificar_fecha_sacramento():
#     id_sacramento = int(input("ID del sacramento: "))
#     nueva_fecha = datetime.strptime(input("Nueva fecha (YYYY-MM-DD): "), "%Y-%m-%d")
#     db.sacramentos.update_one(
#         {"_id": id_sacramento},
#         {"$set": {"fecha": nueva_fecha}}
#     )
#     print("Fecha de sacramento actualizada.")

# # Funciones de eliminación
# def eliminar_inscripcion():
#     id_inscripcion = int(input("ID de la inscripción a eliminar: "))
#     db.inscripciones.delete_one({"_id": id_inscripcion})
#     print("Inscripción eliminada.")

# def eliminar_catequizando():
#     id_catequizando = int(input("ID del catequizando a eliminar: "))
#     db.catequizandos.delete_one({"_id": id_catequizando})
#     print("Catequizando eliminado.")

# def eliminar_certificado():
#     id_certificado = int(input("ID del certificado a eliminar: "))
#     db.certificados.delete_one({"_id": id_certificado})
#     print("Certificado eliminado.")

# def eliminar_catequista():
#     id_catequista = int(input("ID del catequista a eliminar: "))
#     db.catequistas.delete_one({"_id": id_catequista})
#     print("Catequista eliminado.")




# Funciones de consulta
def listar_catequizandos_por_nivel():
    nivel = input("Ingrese el nivel de catecismo: ")
    catequizandos = db.catequizandos.find({"niveles_completados": nivel})
    for c in catequizandos:
        print(f"{c['nombres']} {c['apellidos']} - ID: {c['_id']}")

def buscar_certificados_catequizando():
    id_catequizando = int(input("Ingrese el ID del catequizando: "))
    certificados = db.certificados.find({"catequizando_id": id_catequizando})
    for cert in certificados:
        print(f"Nivel: {cert['nivel_catecismo']}, Fecha: {cert['fecha_emision']}")

def ver_inscripciones_pendientes():
    inscripciones = db.inscripciones.find({"pago_realizado": False})
    for insc in inscripciones:
        catequizando = db.catequizandos.find_one({"_id": insc['catequizando_id']})
        if catequizando:
            print(f"{catequizando['nombres']} {catequizando['apellidos']} - Nivel: {insc['nivel_catecismo']}")

def listar_catequistas_por_parroquia():
    id_parroquia = int(input("Ingrese el ID de la parroquia: "))
    catequistas = db.catequistas.find({"parroquia_id": id_parroquia})
    for cat in catequistas:
        niveles_catecismo = ', '.join(cat.get('niveles_catecismo', []))
        print(f"{cat['nombres']} {cat['apellidos']} - Niveles: {niveles_catecismo}")

def ver_sacramentos_por_fecha():
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    sacramentos = db.sacramentos.find({
        "fecha": {
            "$gte": datetime.strptime(fecha_inicio, "%Y-%m-%d"),
            "$lte": datetime.strptime(fecha_fin, "%Y-%m-%d")
        }
    })
    for sac in sacramentos:
        print(f"Sacramento: {sac['nombre']}, Fecha: {sac['fecha']}")

# Funciones de ingreso
def registrar_catequizando():
    catequizando = {
        "nombres": input("Nombres: "),
        "apellidos": input("Apellidos: "),
        "fecha_nacimiento": datetime.strptime(input("Fecha de nacimiento (YYYY-MM-DD): "), "%Y-%m-%d"),
        "parroquia_actual": int(input("ID de la parroquia: ")),
        "padres": input("Padres (separados por coma): ").split(','),
        "niveles_completados": input("Niveles completados (separados por coma): ").split(','),
        "fe_bautismo": {
            "fecha_bautizo": datetime.strptime(input("Fecha de bautizo (YYYY-MM-DD): "), "%Y-%m-%d"),
            "parroquia_bautizo": input("Parroquia de bautizo: ")
        }
    }
    resultado = db.catequizandos.insert_one(catequizando)
    print(f"Catequizando registrado con ID: {resultado.inserted_id}")

def anadir_inscripcion():
    inscripcion = {
        "catequizando_id": int(input("ID del catequizando: ")),
        "nivel_catecismo": input("Nivel de catecismo: "),
        "fecha_inscripcion": datetime.now(),
        "parroquia_id": int(input("ID de la parroquia: ")),
        "pago_realizado": input("¿Pago realizado? (s/n): ").lower() == 's',
        "fe_bautismo_entregada": input("¿Fe de bautismo entregada? (s/n): ").lower() == 's',
        "caso_especial": {
            "es_especial": input("¿Caso especial? (s/n): ").lower() == 's',
            "descripcion": input("Descripción del caso especial: "),
            "autorizacion_parroco": input("¿Autorización del párroco? (s/n): ").lower() == 's'
        }
    }
    resultado = db.inscripciones.insert_one(inscripcion)
    print(f"Inscripción registrada con ID: {resultado.inserted_id}")

def registrar_certificado():
    certificado = {
        "catequizando_id": int(input("ID del catequizando: ")),
        "nivel_catecismo": input("Nivel de catecismo: "),
        "fecha_emision": datetime.now(),
        "parroquia_id": int(input("ID de la parroquia: ")),
        "catequista_id": int(input("ID del catequista: ")),
        "notas": input("Notas: ")
    }
    resultado = db.certificados.insert_one(certificado)
    print(f"Certificado registrado con ID: {resultado.inserted_id}")

def anadir_catequista():
    catequista = {
        "nombres": input("Nombres: "),
        "apellidos": input("Apellidos: "),
        "parroquia_id": int(input("ID de la parroquia: ")),
        "niveles_catecismo": input("Niveles de catecismo que imparte (separados por coma): ").split(','),
        "anos_experiencia": int(input("Años de experiencia: ")),
        "es_apoyo": input("¿Es apoyo? (s/n): ").lower() == 's'
    }
    resultado = db.catequistas.insert_one(catequista)
    print(f"Catequista registrado con ID: {resultado.inserted_id}")

# Funciones de actualización
def actualizar_pago_inscripcion():
    id_inscripcion = int(input("ID de la inscripción: "))
    nuevo_estado = input("¿Pago realizado? (s/n): ").lower() == 's'
    db.inscripciones.update_one(
        {"_id": id_inscripcion},
        {"$set": {"pago_realizado": nuevo_estado}}
    )
    print("Estado de pago actualizado.")

def cambiar_nivel_catequizando():
    id_catequizando = int(input("ID del catequizando: "))
    nuevo_nivel = input("Nuevo nivel: ")
    db.catequizandos.update_one(
        {"_id": id_catequizando},
        {"$set": {"nivel_actual": nuevo_nivel}}
    )
    print("Nivel de catequizando actualizado.")

def actualizar_contacto_catequista():
    id_catequista = int(input("ID del catequista: "))
    nuevo_telefono = input("Nuevo número de teléfono: ")
    db.catequistas.update_one(
        {"_id": id_catequista},
        {"$set": {"telefono": nuevo_telefono}}
    )
    print("Información de contacto actualizada.")

def modificar_fecha_sacramento():
    id_sacramento = int(input("ID del sacramento: "))
    nueva_fecha = datetime.strptime(input("Nueva fecha (YYYY-MM-DD): "), "%Y-%m-%d")
    db.sacramentos.update_one(
        {"_id": id_sacramento},
        {"$set": {"fecha": nueva_fecha}}
    )
    print("Fecha de sacramento actualizada.")

# Funciones de eliminación
def eliminar_inscripcion():
    id_inscripcion = int(input("ID de la inscripción a eliminar: "))
    db.inscripciones.delete_one({"_id": id_inscripcion})
    print("Inscripción eliminada.")

def eliminar_catequizando():
    id_catequizando = int(input("ID del catequizando a eliminar: "))
    db.catequizandos.delete_one({"_id": id_catequizando})
    print("Catequizando eliminado.")

def eliminar_certificado():
    id_certificado = int(input("ID del certificado a eliminar: "))
    db.certificados.delete_one({"_id": id_certificado})
    print("Certificado eliminado.")

def eliminar_catequista():
    id_catequista = int(input("ID del catequista a eliminar: "))
    db.catequistas.delete_one({"_id": id_catequista})
    print("Catequista eliminado.")




def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '5':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

        if opcion == '1':  # Consultas
            while True:
                mostrar_submenu_consultas()
                subopcion = input("Seleccione una opción: ")
                if subopcion == '1':
                    listar_catequizandos_por_nivel()
                elif subopcion == '2':
                    buscar_certificados_catequizando()
                elif subopcion == '3':
                    ver_inscripciones_pendientes()
                elif subopcion == '4':
                    listar_catequistas_por_parroquia()
                elif subopcion == '5':
                    ver_sacramentos_por_fecha()
                elif subopcion == '6':
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

        elif opcion == '2':  # Ingresos
            while True:
                mostrar_submenu_ingresos()
                subopcion = input("Seleccione una opción: ")
                if subopcion == '1':
                    registrar_catequizando()
                elif subopcion == '2':
                    anadir_inscripcion()
                elif subopcion == '3':
                    registrar_certificado()
                elif subopcion == '4':
                    anadir_catequista()
                elif subopcion == '5':
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

        elif opcion == '3':  # Actualizaciones
            while True:
                mostrar_submenu_actualizaciones()
                subopcion = input("Seleccione una opción: ")
                if subopcion == '1':
                    actualizar_pago_inscripcion()
                elif subopcion == '2':
                    cambiar_nivel_catequizando()
                elif subopcion == '3':
                    actualizar_contacto_catequista()
                elif subopcion == '4':
                    modificar_fecha_sacramento()
                elif subopcion == '5':
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

        elif opcion == '4':  # Eliminaciones
            while True:
                mostrar_submenu_eliminaciones()
                subopcion = input("Seleccione una opción: ")
                if subopcion == '1':
                    eliminar_inscripcion()
                elif subopcion == '2':
                    eliminar_catequizando()
                elif subopcion == '3':
                    eliminar_certificado()
                elif subopcion == '4':
                    eliminar_catequista()
                elif subopcion == '5':
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()