Para resolver el problema, lo he planteado de la siguiente manera:
El número del cual se quiere calcular la fracción irreducible lo almaceno en la variable 'x'.
Como numerador de la fracción multiplico 'x' por 10.000 y denominador = 10.000. Ahora ya tenemos la fracción que representa ese número y sólo queda reducirla.
Para ello, dentro de un bucle while se van probando los disitntos divisores, y cuando tanto en numerador como en denominador devuelven resto = 0 se aplica a la fracción.
De esta forma se asegura que la reducción de la fracción es correcta.
Y así sucesivamente hasta que el bucle acaba cuando ya no encuentra ningún divisor más (francción irreducible),
dándole a la variable 's' el valor de 1 para así salir del bucle while.
