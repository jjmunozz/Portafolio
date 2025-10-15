__name__ = "Juan José Muñoz Jurado"
__email__ = "juan.munozjur@campusucc.eco"
__license__ = "GPL"
__version__ = "1.0.0"

from Mundo.ListaDeContactos import ListaDeContactos

class Menu:
    def __init__(self):
        self.__miListaDeContactos = ListaDeContactos()

    def MenuPrincipal(self):
        salir = False

        while not salir:
            print("----------------------------------------------------------------")
            print("Lista de contactos")
            print("----------------------------------------------------------------")
            print("1. Agregar contacto")
            print("2. Dar todos los contactos")
            print("3. Buscar contacto por palabra clave")
            print("4. Buscar contacto")
            print("5. Eliminar contacto")
            print("6. Modificar contacto")
            print("0. Salir")
            print("----------------------------------------------------------------")

            op = int(input('Digite una opcion: '))

            if op == 1:
                datos = self.SolicitarDatosCompletos()
                print(('no agregado', 'agregado con exito')[self.__miListaDeContactos.agregarContacto(*datos)])
            elif op == 2:
                contactos = self.__miListaDeContactos.darTodosLosContactos()
                for contacto in contactos:
                    print(contacto)
            elif op == 3:
                palabra = input('Digite palabra clave: ')
                encontrados = self.__miListaDeContactos.buscarContactosPalabraClave(palabra)
                for c in encontrados:
                    print(c)
            elif op == 4:
                nombre = input('Digite nombre: ')
                apellido = input('Digite apellido: ')
                contacto = self.__miListaDeContactos.buscarContacto(nombre, apellido)
                if contacto:
                    print("Datos:", contacto.darNombre(), contacto.darApellido())
                    print("Dirección:", contacto.darDireccion())
                    print("Correo electrónico:", contacto.darCorreo())
                    print("Teléfonos:", contacto.darTelefonos())
                    print("Palabras clave:", contacto.darPalabras())
                else:
                    print("Contacto no encontrado.")
            elif op == 5:
                if self.__miListaDeContactos.eliminarContacto(input('Nombre: '), input('Apellido: ')):
                    print("Contacto eliminado.")
                else:
                    print("Contacto no encontrado.")
            elif op == 6:
                datos = self.SolicitarDatosCompletos()
                if self.__miListaDeContactos.modificarContacto(*datos):
                    print("Contacto modificado.")
                else:
                    print("Contacto no encontrado.")
            elif op == 0:
                salir = True

        return "Adios"

    def SolicitarDatosCompletos(self):
        nombre = input('Digite nombre: ')
        apellido = input('Digite apellido: ')
        direccion = input('Digite direccion: ')
        correo = input('Digite correo: ')
        telefonos = self.AgregarTelefonos()
        palabras = self.AgregarPalabras(nombre, apellido)
        return [nombre, apellido, direccion, correo, telefonos, palabras]

    def AgregarTelefonos(self):
        salir = False
        telefonos = []

        while not salir:
            telefono = input('Digite telefono: ')
            if telefono.isdigit():
                telefonos.append(telefono)
            else:
                print('No es un número de teléfono')

            op = int(input('Desea agregar otro telefono? si=1, no=2: '))
            if op == 2:
                salir = True

        return telefonos

    def AgregarPalabras(self, nombre, apellido):
        palabras = [nombre, apellido]
        return palabras

if __name__ == "__main__":
    menu = Menu()
    print(menu.MenuPrincipal())