class Contacto:
    __method__ = "__init__"
    __params__ = "nombre: str, apellido: str, direccion: str, correo: str"
    __description__ = "Inicializa un nuevo contacto con nombre, apellido, dirección y correo."
    __return__ = "None"
    def __init__(self, nombre, apellido, direccion, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__correo = correo
        self.__telefonos = []
        self.__palabrasClave = []

    __method__ = "darNombre"
    __params__ = "None"
    __description__ = "Devuelve el nombre del contacto."
    __return__ = "str"
    def darNombre(self):
        return self.__nombre

    __method__ = "darApellido"
    __params__ = "None"
    __description__ = "Devuelve el apellido del contacto."
    __return__ = "str"
    def darApellido(self):
        return self.__apellido

    __method__ = "darDireccion"
    __params__ = "None"
    __description__ = "Devuelve la dirección del contacto."
    __return__ = "str"
    def darDireccion(self):
        return self.__direccion

    __method__ = "darCorreo"
    __params__ = "None"
    __description__ = "Devuelve el correo electrónico del contacto."
    __return__ = "str"
    def darCorreo(self):
        return self.__correo

    __method__ = "darTelefonos"
    __params__ = "None"
    __description__ = "Devuelve la lista de teléfonos del contacto."
    __return__ = "list[str]"
    def darTelefonos(self):
        return self.__telefonos

    __method__ = "darPalabras"
    __params__ = "None"
    __description__ = "Devuelve la lista de palabras clave del contacto."
    __return__ = "list[str]"
    def darPalabras(self):
        return self.__palabrasClave

    __method__ = "cambiarDireccion"
    __params__ = "direccion: str"
    __description__ = "Cambia la dirección del contacto."
    __return__ = "None"
    def cambiarDireccion(self, direccion):
        self.__direccion = direccion

    __method__ = "cambiarCorreo"
    __params__ = "correo: str"
    __description__ = "Cambia el correo del contacto."
    __return__ = "None"
    def cambiarCorreo(self, correo):
        self.__correo = correo

    __method__ = "agregarTelefono"
    __params__ = "telefono: str"
    __description__ = "Agrega un número telefónico al contacto."
    __return__ = "None"
    def agregarTelefono(self, telefono):
        if telefono not in self.__telefonos:
            self.__telefonos.append(telefono)

    __method__ = "eliminarTelefono"
    __params__ = "telefonoEliminar: str"
    __description__ = "Elimina un número telefónico del contacto."
    __return__ = "None"
    def eliminarTelefono(self, telefonoEliminar):
        if telefonoEliminar in self.__telefonos:
            self.__telefonos.remove(telefonoEliminar)

    __method__ = "agregarPalabra"
    __params__ = "palabra: str"
    __description__ = "Agrega una palabra clave al contacto."
    __return__ = "None"
    def agregarPalabra(self, palabra):
        if palabra not in self.__palabrasClave:
            self.__palabrasClave.append(palabra)

    __method__ = "eliminarPalabra"
    __params__ = "palabraEliminar: str"
    __description__ = "Elimina una palabra clave del contacto."
    __return__ = "None"
    def eliminarPalabra(self, palabraEliminar):
        if palabraEliminar in self.__palabrasClave:
            self.__palabrasClave.remove(palabraEliminar)

    __method__ = "contienePalabraClave"
    __params__ = "palabra: str"
    __description__ = "Verifica si el contacto contiene una palabra clave."
    __return__ = "bool"
    def contienePalabraClave(self, palabra):
        return palabra in self.__palabrasClave

    def __str__(self):
        return f"{self.__nombre} {self.__apellido} - Dirección: {self.__direccion}, Correo: {self.__correo}, Teléfonos: {', '.join(self.__telefonos)}, Palabras clave: {', '.join(self.__palabrasClave)}"
