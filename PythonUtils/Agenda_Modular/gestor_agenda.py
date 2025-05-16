# LÓGICA DE LA AGENDA
agenda = []

def agregar_contacto(contacto):
    agenda.append(contacto)

def buscar_contacto(nombre):
    return [c for c in agenda if c.nombre.lower() == nombre.lower()]

def eliminar_contacto(nombre):
    global agenda
    agenda = [c for c in agenda if c.nombre.lower() != nombre.lower()]

def listar_contactos():
    return agenda

