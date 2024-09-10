nombre = input("Dime tu nombre: ")
ventas = int(input("Valor total que vendiste este mes: "))
valor_comision = round(ventas * 13 / 100, 2)

print(f"{nombre} el valor total de tus ventas con las comisiones es de ${valor_comision}")
