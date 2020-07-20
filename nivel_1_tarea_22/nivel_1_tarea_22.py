from itertools import combinations #módulo para realizar combinaciones de elementos

vacas= [977.33953798, 2060.72066683, 798.22057087, 1400.78778956, 2591.93334107, 1187.35223672, 500, 700] #Pesos de las vacas
litros_dia= [73.01229011, 34.74282537, 73.06971073, 81.65602756, 13.58612572, 18.90415454, 40, 33] #Producción en litros/día de las vacas
pcamion=4000 #peso máximo que admite el camión
num_vacas=8 #número de vacas disponibles para comprar
prod_final=0 #incializo la variable con valor 0

for i in range(2,num_vacas+1): #Se realizan las combinaciones de elementos en grupos desde 2 elementos hasta grupos del num_vacas
	#print('grupos de ',i)
	combinaciones_peso = list(combinations(vacas,i)) #Combinaciones de los pesos
	combinaciones_litros_dia = list(combinations(litros_dia,i)) #Combinaciones de la producción respectiva
	#print(combinaciones_peso)
	#print('número de grupos: ',len(combinaciones_peso))
	for j in range(len(combinaciones_peso)): 
		#print(combinaciones_peso[j])
		#print('suma de peso: ',sum(combinaciones_peso[j]))
		if(sum(combinaciones_peso[j]) <= pcamion): #Para cada combinación se compara el peso con el máximo del camión, y si es peso menor se actualiza la variable prod_final siempre y cuando sea mayor que el valor que ya tenia alamacenado
			if(prod_final <= sum(combinaciones_litros_dia[j])):
				prod_final=sum(combinaciones_litros_dia[j])


print(f'La producción máxima son {prod_final} litros/día')





