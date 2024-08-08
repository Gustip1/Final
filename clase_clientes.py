class clientes:
    __nombre:str
    __apellido:str
    __email:str
    __contrasena:str
    __direccion_postal:str  
    __telefono:str
    
    def __init__(self, nombre, apellido, email, contrasena, direccion_postal, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasena = contrasena
        self.__direccion_postal = direccion_postal
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_email(self):
        return self.__email

    def get_contrasena(self):
        return self.__contrasena

    def get_direccion_postal(self):
        return self.__direccion_postal

    def get_telefono(self):
        return self.__telefono

    def __str__(self):
        return (f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, "
                f"Email: {self.__email}, Dirección Postal: {self.__direccion_postal}, "
                f"Teléfono: {self.__telefono}")
