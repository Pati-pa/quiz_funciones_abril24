# Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

print("--------------------------------")
print("-- Verificación de ultimo digito LISTA DATOS --")
print("--------------------------------")

#Definición de la función
def determinar_digito(n):   
    if n %10 == 4 :
        print( f"el ultimo digito de {n} si es 4")
    else :
        print(f"el ultimo digito de {n} no es 4")
    return n



#Entrada
n = int(input("Ingrese el valor entero: "))

#Salida
determinar_digito(n)
print("\nEso era...")