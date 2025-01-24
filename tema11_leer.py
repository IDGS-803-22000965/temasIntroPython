from io import open

texto=""

archivo=open("archivo.txt","r")


"""texto=archivo.read()
print(texto)

archivo.seek(0)
texto=archivo.read()
print(texto)
"""


texto=archivo.readline()
print(texto)
archivo.close()
