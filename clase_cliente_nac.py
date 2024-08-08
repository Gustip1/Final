from clase_clientes import clientes
class cliente_nac(clientes):
    __provincia:str
    __localidad:str
    __codigo_postal:str
    def __init__(self, nombre, apellido, email, contrasena, direccion_postal, telefono, provincia, localidad, codigo_postal):
        super().__init__(nombre, apellido, email, contrasena, direccion_postal, telefono)
        self.__provincia = provincia
        self.__localidad = localidad
        self.__codigo_postal = codigo_postal

    def get_provincia(self):
        return self.__provincia

    def get_localidad(self):
        return self.__localidad

    def get_codigo_postal(self):
        return self.__codigo_postal

    def __str__(self):
        return (f"{super().__str__()}, Provincia: {self.__provincia}, "
                f"Localidad: {self.__localidad}, Código Postal: {self.__codigo_postal}")
