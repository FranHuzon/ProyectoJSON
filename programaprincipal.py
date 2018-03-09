import json

with open("salud_mental_Gijon.json") as fichero:
	datos=json.load(fichero)

dic=datos["array"]["directorios"]["directorio"]
print(dic)