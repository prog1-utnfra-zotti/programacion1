from inicio_sesion import iniciar_sesion

print("Bienvenidos a la tienda virtual")



# Función principal para el menú
def menu_principal():
    print("Bienvenido al sistema")
    
    if iniciar_sesion():
        while True:
            print("\nMenú Principal")
            print("1. Comprar")
            print("2. Salir")
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                pass # aca ira realizar_compra()
            elif opcion == "2":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intenta nuevamente.")

# Ejecutar el menú principal
menu_principal()




print("Gracias por visitar!!!!!")


print("Gracias")


print("Gracias por visitar nuestra tienda virtual")
