class Diccionario:
    
    nombre_archivo = ""
    palabras = {}
    
    def __init__(self, archivo):
        self.archivo = archivo
        self.palabras = {}
        self.cargar_palabras()

    def agregar_palabra(self, esp, ing):
        self.palabras[esp] = ing
        self.guardar_cambios()

    def buscar_palabra(self):
        while (opcion := input("Buscar en:\n1. Español\n2. Inglés\nOpción: ")) not in ["1", "2"]:
            print("Opción inválida. Elige 1 o 2.")

        palabra = input("Ingrese la palabra a buscar: ")

        if opcion == "1":
            print(f"La traducción de {palabra} es: {self.palabras.get(palabra, 'No encontrada')}")
        else:
            traduccion = next((esp for esp, ing in self.palabras.items() if ing == palabra), None)
            print(f"La traducción de {palabra} es: {traduccion if traduccion else 'No encontrada'}")

    def guardar_cambios(self):
        with open(self.archivo, "w") as f:
            f.writelines(f"{esp}|{ing}\n" for esp, ing in self.palabras.items())

    def cargar_palabras(self):
        try:
            with open(self.archivo, "r") as f:
                self.palabras = dict(linea.strip().split("|") for linea in f)
        except FileNotFoundError:
            print("Archivo no encontrado. Creando uno nuevo.")
    
    def menu(self):
        while True:
            opcion = input("\n1. Agregar palabra\n2. Buscar palabra\n3. Salir\nSeleccione una opción: ")

            if opcion == "1":
                dic.agregar_palabra(input("Ingrese la palabra en español: "), input("Ingrese la palabra en inglés: "))
            elif opcion == "2":
                 dic.buscar_palabra()
            elif opcion == "3":
                break
            else:
                 print("Opción inválida.")




if __name__ == "__main__":
    dic = Diccionario("diccionario.txt")
    dic.menu()
    