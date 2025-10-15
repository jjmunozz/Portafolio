from Mundo.Contacto import Contacto

class ListaDeContactos:
    __method__ = "__init__"
    __params__ = "None"
    __description__ = "Inicializa una lista vacía de contactos."
    __return__ = "None"
    def __init__(self):
        self.__contactos = []

    __method__ = "darTodosLosContactos"
    __params__ = "None"
    __description__ = "Retorna la lista completa de contactos."
    __return__ = "list[Contacto]"
    def darTodosLosContactos(self):
        return [f"{c.darNombre()} {c.darApellido()}" for c in self.__contactos]

    __method__ = "buscarContactosPalabraClave"
    __params__ = "palabra: str"
    __description__ = "Busca todos los contactos que contienen una palabra clave dada."
    __return__ = "list[Contacto]"
    def buscarContactosPalabraClave(self, palabra):
        resultado = []
        for c in self.__contactos:
            if (
                palabra.lower() in c.darNombre().lower()
                or palabra.lower() in c.darApellido().lower()
                or palabra.lower() in c.darDireccion().lower()
                or palabra.lower() in c.darCorreo().lower()
                or any(palabra.lower() in p.lower() for p in c.darPalabras())
            ):
                resultado.append(f"{c.darNombre()} {c.darApellido()}")
        return resultado

    __method__ = "buscarContacto"
    __params__ = "nombre: str, apellido: str"
    __description__ = "Busca un contacto por su nombre y apellido."
    __return__ = "Contacto or None"
    def buscarContacto(self, nombre, apellido):
        for c in self.__contactos:
            if c.darNombre() == nombre and c.darApellido() == apellido:
                return c
        return None

    __method__ = "agregarContacto"
    __params__ = "nombre, apellido, direccion, correo, telefonos, palabras"
    __description__ = "Agrega un nuevo contacto si no existe otro con el mismo nombre y apellido."
    __return__ = "bool"
    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido):
            return False
        contacto = Contacto(nombre, apellido, direccion, correo)
        self.actualizarTelefonos(telefonos, contacto)
        self.actualizarPalabras(palabras, contacto)
        self.__contactos.append(contacto)
        return True

    __method__ = "eliminarContacto"
    __params__ = "nombre: str, apellido: str"
    __description__ = "Elimina un contacto de la lista."
    __return__ = "bool"
    def eliminarContacto(self, nombre, apellido):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            self.__contactos.remove(contacto)
            return True
        return False

    __method__ = "modificarContacto"
    __params__ = "nombre, apellido, direccion, correo, telefonos, palabras"
    __description__ = "Modifica la información de un contacto existente."
    __return__ = "bool"
    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            contacto.cambiarDireccion(direccion)
            contacto.cambiarCorreo(correo)
            self.actualizarTelefonos(telefonos, contacto)
            self.actualizarPalabras(palabras, contacto)
            return True
        return False

    __method__ = "actualizarTelefonos"
    __params__ = "telefonos: list[str], contacto: Contacto"
    __description__ = "Actualiza la lista de teléfonos del contacto."
    __return__ = "None"
    def actualizarTelefonos(self, telefonos, contacto):
        contacto._Contacto__telefonos.clear()
        for tel in telefonos:
            contacto.agregarTelefono(tel)

    __method__ = "actualizarPalabras"
    __params__ = "palabras: list[str], contacto: Contacto"
    __description__ = "Actualiza las palabras clave del contacto."
    __return__ = "None"
    def actualizarPalabras(self, palabras, contacto):
        contacto._Contacto__palabrasClave.clear()
        for pal in palabras:
            contacto.agregarPalabra(pal)
