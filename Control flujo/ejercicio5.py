"""5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número 
no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de 
números y notificarlo:

Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista 
(devuelve True o False)"""

lista = [1, 3, 6, 9]

while True:
    numero = int(input("Ingresar un número del 0 al 9: "))
    if numero >= 0 and numero <= 9:
        break
if numero in lista:
    print("El número",numero,"se encuentra en la lista",lista)
else:
    print("El número",numero,"no se encuentra en la lista",lista)