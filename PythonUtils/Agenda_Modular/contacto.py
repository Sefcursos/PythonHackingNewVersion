# CLASE QUE DEFINE QUÉ ES UN CONTACTO

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.email}"