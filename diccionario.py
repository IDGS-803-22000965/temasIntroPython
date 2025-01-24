class Diccionario:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.palabras = {}

    def agregar_palabra(self, palabra_esp, palabra_ing):
        self.palabras[palabra_esp] = palabra_ing
        self.guardar_cambios()

    def buscar_palabra(self):
        while True:
            opcion_idioma = input("Buscar en:\n1. Español\n2. Inglés\nOpción: ")
            if opcion_idioma in ["1", "2"]:
                break
            else:
                print("Opción inválida. Por favor, elige 1 o 2.")

        palabra_buscar = input("Ingrese la palabra a buscar: ")

        if opcion_idioma == "1":
            if palabra_buscar in self.palabras:
                print(f"La traducción de {palabra_buscar} es: {self.palabras[palabra_buscar]}")
            else:
                print("Palabra no encontrada en español.")
        else:
            for esp, ing in self.palabras.items():
                if ing == palabra_buscar:
                    print(f"La traducción de {palabra_buscar} es: {esp}")
                    return
            print("Palabra no encontrada en inglés.")

    def guardar_cambios(self):
        with open(self.nombre_archivo, "w") as archivo:
            for esp, ing in self.palabras.items():
                archivo.write(f"{esp}|{ing}\n")

    def cargar_palabras(self):
        try:
            with open(self.nombre_archivo, "r") as archivo:
                for linea in archivo:
                    esp, ing = linea.strip().split("|")
                    self.palabras[esp] = ing
        except FileNotFoundError:
            print("Archivo no encontrado. Creando uno nuevo...")

if __name__ == "__main__":
    diccionario = Diccionario("mi_diccionario.txt")
    diccionario.cargar_palabras()

    while True:
        print("\n1. Agregar palabra")
        print("2. Buscar palabra")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            esp = input("Ingrese la palabra en español: ")
            ing = input("Ingrese la palabra en inglés: ")
            diccionario.agregar_palabra(esp, ing)
        elif opcion == "2":
            diccionario.buscar_palabra()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")