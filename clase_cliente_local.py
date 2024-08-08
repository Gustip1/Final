from clase_clientes import clientes

class cliente_local(clientes):
    def __init__(self, nombre, apellido, email, contrasena, direccion_postal, telefono):
        super().__init__(nombre, apellido, email, contrasena, direccion_postal, telefono)

    def __str__(self):
        return super().__str__()
