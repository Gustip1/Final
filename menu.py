from clase_gestor import lista
from clase_cliente_local import cliente_local
from clase_cliente_nac import cliente_nac
class unmenu:
    def __init__(self):
        self.GL = lista()

    def run(self):
        while True:
            a = input("""MENU DE OPCIONES
1 para agregar cliente y mostrar todos los clientes:
2 para mostrar clientes nacionales:
3 para consultar tipo de cliente en una posición:
4 para salir:
Seleccione una opción: """)
            if a == '1':
                self.agregar_cliente()
                print("\nClientes en la lista:")
                self.GL.mostrar_clientes()
            elif a == '2':
                print("\nClientes Nacionales:")
                self.GL.buscar_cliente_nacional()
            elif a == '3':
                self.GL.posicion()
            elif a == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def agregar_cliente(self):
        cliente_tipo = input("Ingrese el tipo de Cliente, L para locales y N para nacionales: ")
        nombre = input("Ingrese nombre: ") 
        apellido = input("Ingrese apellido:")  
        email = input("Ingrese email:")
        contraseña = input("Ingrese contraseña: ")
        direccion_postal = input("Ingrese la direccion postal:")
        telefono = input("Ingrese el telefono:")

        if cliente_tipo == "L":
            nuevo_cliente = cliente_local(nombre, apellido, email, contraseña, direccion_postal, telefono)
            self.GL.insertar_final(nuevo_cliente)
            print("El cliente local fue agregado exitosamente.")
        elif cliente_tipo == "N":
            provincia = input("Ingrese la provincia: ")
            localidad = input("Ingrese la localidad:")
            codigo_postal = input("Ingrese el código postal:")
            nuevo_cliente = cliente_nac(nombre, apellido, email, contraseña, direccion_postal, telefono, provincia, localidad, codigo_postal)
            self.GL.insertar_final(nuevo_cliente)
            print("El cliente nacional fue agregado exitosamente.")
        else:
            print("Tipo de cliente no válido. Intente de nuevo.")
