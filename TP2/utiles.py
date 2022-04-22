def vocales (cadena):
    print(list(filter(lambda l: l.lower() in "aeiou",cadena)))


import json

archivo = open("bandas.txt", "w")
datos = [
{"nombre": "William Campbell", "ciudad": "La Plata", "ref": "www.instagram.com/williamcampbellok"},
{"nombre": "Buendia", "ciudad": "La Plata", "ref":"https://buendia.bandcamp.com/"},
{"nombre": "Lúmine", "ciudad": "La Plata", "ref": "https://www.instagram.com/luminelp/"}]
print(type(datos))
json.dump(datos, archivo)
archivo.close()


archivo = open("bandas.txt", "r")
datos = json.load(archivo)
#print(type(datos))
#print(datos)
datos_a_mostrar = json.dumps(datos, indent=4)
print(datos_a_mostrar)
print(type(datos_a_mostrar))
archivo.close()
