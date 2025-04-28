def iniciar_sesion():
    usuario = "usuario123"
    contrasena = "password"

    print("Inicio de Sesión")
    user = input("Nombre de usuario: ")
    pwd = input("Contraseña: ")

    if user == usuario and pwd == contrasena:
        print("Inicio de sesión exitoso.")
        return True
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return False