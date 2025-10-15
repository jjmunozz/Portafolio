import pytest
from Mundo.Contacto import Contacto
from Mundo.ListaDeContactos import ListaDeContactos

@pytest.fixture
def setup_escenario1():
    contacto1 = Contacto("Carolina", "Rodríguez", "Trv 25 No. 43 - 45", "crodriguez@campusucc.edu.co")
    contacto1.agregarTelefono("6556850")
    contacto1.agregarTelefono("4859527")
    contacto1.agregarPalabra("Amigos")
    contacto1.agregarPalabra("Fiesta")

    contacto2 = Contacto("Camila", "Borrero", "Cll 56 No. 67 - 76", "cborrero@campusucc.edu.co")
    contacto2.agregarTelefono("6456787")
    contacto2.agregarTelefono("5678765")
    contacto2.agregarPalabra("Amigas")
    contacto2.agregarPalabra("Fiesta")

    contacto3 = Contacto("Mauricio", "Sánchez", "Av 24 No. 6 - 32", "msanchez@msanchez.com")
    contacto3.agregarTelefono("6785465")
    contacto3.agregarPalabra("Papa")
    contacto3.agregarPalabra("Familia")

    lista = ListaDeContactos()
    lista.agregarContacto(contacto1.darNombre(), contacto1.darApellido(), contacto1.darDireccion(), contacto1.darCorreo(), contacto1.darTelefonos(), contacto1.darPalabras())
    lista.agregarContacto(contacto2.darNombre(), contacto2.darApellido(), contacto2.darDireccion(), contacto2.darCorreo(), contacto2.darTelefonos(), contacto2.darPalabras())
    lista.agregarContacto(contacto3.darNombre(), contacto3.darApellido(), contacto3.darDireccion(), contacto3.darCorreo(), contacto3.darTelefonos(), contacto3.darPalabras())

    return lista, contacto1, contacto2, contacto3

def test_dar_todos_los_contactos(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    contactos = lista.darTodosLosContactos()
    assert contactos == ["Carolina Rodríguez", "Camila Borrero", "Mauricio Sánchez"]

def test_dar_contactos_palabra(setup_escenario1):
    lista, _, _, _ = setup_escenario1

    contactos = lista.buscarContactosPalabraClave("Fiesta")
    assert contactos == ["Carolina Rodríguez", "Camila Borrero"]

    contactos = lista.buscarContactosPalabraClave("Familia")
    assert contactos == ["Mauricio Sánchez"]

    contactos = lista.buscarContactosPalabraClave("Camila")
    assert contactos == ["Camila Borrero"]

def test_buscar_contacto_existente(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    c = lista.buscarContacto("Camila", "Borrero")
    assert c is not None
    assert c.darNombre() == "Camila"
    assert c.darApellido() == "Borrero"
    assert c.darTelefonos() == ["6456787", "5678765"]

def test_buscar_contacto_inexistente(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    c = lista.buscarContacto("Pedro", "Pérez")
    assert c is None

def test_contacto_duplicado(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    resultado = lista.agregarContacto("Camila", "Borrero", "otra dir", "otro@mail.com", [], [])
    assert resultado is False

def test_eliminar_contacto(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    assert not lista.eliminarContacto("Diana", "Puentes")
    assert lista.eliminarContacto("Mauricio", "Sánchez")
    contactos = lista.buscarContactosPalabraClave("Familia")
    assert len(contactos) == 0

def test_modificar_contacto(setup_escenario1):
    lista, _, _, _ = setup_escenario1

    assert not lista.modificarContacto("Pedro", "Sánchez", "Nueva dirección", "nuevo@correo.com", [], [])

    lista.modificarContacto("Mauricio", "Sánchez", "Av 24 No. 6 - 44", "msanchez1@msanchez.com", [], [])
    c = lista.buscarContacto("Mauricio", "Sánchez")
    assert c.darDireccion() == "Av 24 No. 6 - 44"
    assert len(c.darPalabras()) == 0
    assert len(c.darTelefonos()) == 0
