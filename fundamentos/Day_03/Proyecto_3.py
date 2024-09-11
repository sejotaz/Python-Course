texto = input('Ingresar texto: ').lower()
print(texto)
list_letter = []

list_letter.append(input('Ingresa la primera letra : ').lower())

list_letter.append(input('Ingresa la segunda letra : ').lower())

list_letter.append(input('Ingresa la tercera letra : ').lower())

print('\n')
print('CANTIDAD DE LETRAS')
cantidad_letras1 = texto.count(list_letter[0])
cantidad_letras2 = texto.count(list_letter[1])
cantidad_letras3 = texto.count(list_letter[2])
print(f'La letra es "{list_letter[0]}" y la cantidad de veces de la letra 1: {cantidad_letras1}')
print(f'La letra es "{list_letter[1]}" y la cantidad de veces de la letra 2: {cantidad_letras2}')
print(f'La letra es "{list_letter[2]}" y la cantidad de veces de la letra 3: {cantidad_letras3}')

print('\n')
print('CANTIDAD DE PALABRAS')
palabras = texto.split()
print(f'2. Hemos encontrado {len(palabras)} palabras en tu texto')

print('\n')
print('LETRAS DE INICIO Y DE FIN')
print(f'3. La primera letra del texto es "{texto[0]}"\n La ultima letra del texto es "{texto[-1]}"')


print('\n')
print('TEXTO INVERTIDO')
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f'4. Si ordenamos tu texto al revés va a decir "{texto_invertido}"')

print('\n')
print('BUSCANDO LA PALABRA')
search_python = 'python' in texto
dic = {True: 'Si', False: 'No'}
print(f'La palabra "Python" {dic[search_python]} Se encuentra en el texto')


