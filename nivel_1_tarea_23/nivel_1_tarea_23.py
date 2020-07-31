import random

mensaje = 'Han descifrado enigma' #No se puede escribir ningún mensaje que contenga la letra Ñ
print(mensaje)
mensaje = mensaje.upper() #convertir letras a mayúsculas
mensaje = mensaje.replace(' ','') #Elimina todos los espacios del string

#número de 'X' a añadir al mensaje antes de cifrar
resto = len(mensaje) % 5
añade_X = 0 
if (resto != 0):
	añade_X = 5-resto 
	
#añadiendo las 'X'
for i in range(1, añade_X+1): 
	mensaje = mensaje +'X'

#print(mensaje)
longitud = len(mensaje)
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def generar_ristra(): #Se genera con él módulo random de python en vez de usar el método de la baraja
	ristra = []
	for i in range(len(mensaje)):
		j = random.randint(0,25)
		ristra.append(letras[j])
	ristra = ''.join(ristra)

	return ristra



def cifrar_mensaje():
	#ristra = ('KRCBUQSTHLOVCMT')
	#print(ristra)
	mensaje_numeros = [(ord(i) - 96) for i in mensaje.lower()] #convertir mensaje a números
	ristra_numeros = [(ord(i) - 96) for i in ristra.lower()] #convertir ristra a números
	#print(mensaje_numeros)
	#print(ristra_numeros)
	
	sumanumeros = []
	mensaje_cifrado = []
	#sumar mensaje y ristra módulo 26
	for i in range(longitud): 
		sumanumeros.append(mensaje_numeros[i]+ristra_numeros[i])
		if (sumanumeros[i] > 26):
			sumanumeros[i] = sumanumeros[i] - 26

	#print(f'Suma = {sumanumeros}')	

	#convertir mensaje a letras
	for i in sumanumeros: 	
		mensaje_cifrado.append(letras[i-1])

	mensaje_cifrado = ''.join(mensaje_cifrado)
	#print(mensaje_cifrado)

	# DIVIDIR MENSAJE Y UNIR
	n=5 
	mensaje_cifrado_entregado = [(mensaje_cifrado[i:i+n]) for i in range(0, len(mensaje_cifrado), n)] #divide el string en grupos de 'n' caracteres
	mensaje_cifrado_entregado = ' '.join(mensaje_cifrado_entregado)	#une el mensaje con todos los trozos dejando espacio en blanco entre cada trozo
	print(f'Mensaje cifrado entregado: {mensaje_cifrado_entregado}')
	
	return mensaje_cifrado



def descrifrar_mensaje():
	#print(mensaje_cifrado)
	#print(ristra)

	mensaje_numeros = [(ord(i) - 96) for i in mensaje_cifrado.lower()] #convertir mensaje cifrado a números
	ristra_numeros = [(ord(i) - 96) for i in ristra.lower()] #convertir ristra a números
	#print(mensaje_numeros)
	#print(ristra_numeros)

	restanumeros = []
	mensaje_descifrado = []
	#restar mensaje y ristra módulo 26
	for i in range(longitud): 
		restanumeros.append(mensaje_numeros[i]-ristra_numeros[i])
		if (restanumeros[i] <= 0):
			restanumeros[i] = restanumeros[i] + 26

	#print(f'Resta = {restanumeros}')

	#convertir mensaje a letras
	for i in restanumeros: 	
		mensaje_descifrado.append(letras[i-1])

	mensaje_descifrado = ''.join(mensaje_descifrado)
	#print(mensaje_descifrado)

	# DIVIDIR MENSAJE Y UNIR
	n=5 
	mensaje_descifrado_obtenido = [(mensaje_descifrado[i:i+n]) for i in range(0, len(mensaje_descifrado), n)] #divide el string en grupos de 'n' caracteres
	mensaje_descifrado_obtenido = ' '.join(mensaje_descifrado_obtenido)	#une el mensaje con todos los trozos dejando espacio en blanco entre cada trozo
	print(f'Mensaje descifrado obtenido: {mensaje_descifrado_obtenido}')
	
	return mensaje_descifrado_obtenido


ristra = generar_ristra()
mensaje_cifrado = cifrar_mensaje()
solucion = descrifrar_mensaje()
#print(solucion)


#Mirar diccionarios de python para el cambio de letras anúmeros y viceversa.