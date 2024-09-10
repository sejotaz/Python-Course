diccionario = {'c1': 'valor1', 'c2': 'valor2'}

resultado = diccionario['c1']

print(resultado)

cliente = {'nombre': 'Juan', 'apellido': 'Fuentes', 'peso' : 88, 'talla': 1.76}
consulta = (cliente['apellido'])
print(consulta)

dic = {'c1':55, 'c2': [10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

#Ejercicio
dicc = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dicc['c2'][1].upper())

diccc = {1: 'a', 2: 'b'}
diccc[3] =  'c'

print(diccc)


#Sobreescribir

diccc[2] = 'B'

print(diccc)


print(diccc.keys())
print(diccc.values())
print(diccc.items())


mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad'] = 36
print(mi_dic)
