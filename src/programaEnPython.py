def pedirNombre():
    nombre = input("¿Cuál es tu nombre? ")
    return nombre
    
def saludarAlUsuario(nombre):
    print(f"Hola {nombre}. Este programa está hecho en el lenguaje de programación: Python.")

#Programa principal
def main():
    
    #Entrada
    nombre= pedirNombre()
    #Salida
    saludarAlUsuario(nombre)

if __name__ == "__main__":
    main()