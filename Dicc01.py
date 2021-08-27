d1 = {
  "Nombre": "Camilo",
  "Edad": 22,
  "Documento": 12345
}
d2 = {
  "Nombre": "Camilo",
  "Edad": 22,
  "Documento": 12345,
  "Email": "camilo@gmail.com"
}
d1.pop('Edad')
d1.update(d2)
print(d1)
##keys=d1.keys()
##valores=d1.values()
##print(list(keys))
##print(list(valores))
##print(d1)
##d1['Nombre']="Pedro"
##print(d1['Nombre'])
##for item in d1:
##    print(item)
##for key in d1:
##    print(d1[key])
##for key,valor in d1.items():
##    print(f"key:[{key}] valor:[{valor}]")
##d1.clear()
##lstD1=d1.items()
##print(lstD1)
##print(list(lstD1))
##print(list(lstD1)[0][0])
##print(d1.get('Nombre'))
##print(d1.get('Email','El correo no existe'))
