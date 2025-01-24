from io import open

texto="una linea nueva con a"

archivo=open("archivo.txt","a")
archivo.write(texto)
#texto="\nuna linea Nueva"
#archivo.write(texto)
#texto="\nuna linea Nueva tres"
#archivo.write(texto)
archivo.close()