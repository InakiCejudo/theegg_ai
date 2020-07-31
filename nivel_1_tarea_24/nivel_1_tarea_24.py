#DE NÚMERO EN DECIMAL A BINARIO

num_10 = 23 #Este es el número en base decimal a calcular. Se puede editar para probar cualquier número.
print(f'El número en base decimal es: {num_10}')
restos = []
cociente = int(num_10 / 2) #si la división no es exacta se redondea hacia abajo para convertir en entero
resto = num_10 % 2

while(cociente >= 1): #bucle para ir diviendo entre 2 todo el rato y formar el array en binario

	#print(resto,cociente)	
	restos.append(resto) #se van añadiendo los sucesivos restos a un array
	num_10 = cociente
	cociente = int(num_10 / 2) #si la división no es exacta se redondea hacia abajo para convertir en entero	
	resto = num_10 % 2
	
	

restos.append(1) #último cociente siempre es 1 y hay que añadirlo

#Ordenar el número binario (hemos ido almacenandolo en orden inverso)
num_2 = []
j = len(restos)
for i in range (len(restos)):	
	num_2.append(restos[j-1])
	j = j-1

num_2 = ''.join(str(e) for e in num_2) #from array to string
print(f'En binario es: {num_2}')
