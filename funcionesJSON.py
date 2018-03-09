import json

with open("salud_mental_Gijon.json") as fichero:
	datos=json.load(fichero)

dic=datos["array"]["directorios"]["directorio"]

def nombres_centros():
	for i in dic:
		print(i[])


print(nombres_centros())