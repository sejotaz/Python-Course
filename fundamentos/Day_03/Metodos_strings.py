texto = "Este es el texto de Alejo"
resultado = texto

#Se puede hacer slicing
print(resultado[2].upper())
#--------------
print(resultado.lower())
#--------------
#Recibe parametro que es un criterio de separación a aplicar
print(resultado.split("t"))
#--------------
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)

#-------------
#Si no encuentra lo que buscas en el texto va a devolver -1
print(resultado.find("s"))
#------------------------
#Recibe dos parametros. 1 es el valor reemplazar y el segundo es el valor que nuevo que reemplaza
print(resultado.replace("Alejo", "Sejotaz"))


