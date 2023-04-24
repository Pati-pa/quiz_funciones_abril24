# Construir una función que reciba un valor entero como parámetro y muestra la tabla de multiplicar de dicho valor recibido. 

print("--------------------------------")
print("-- Tabla multiplicar LISTA DATOS --")
print("--------------------------------")

#Definición de la función
def calcular_tabla(x):
    for i in range(1,11):
        print(x,"*", i, "=", x*i)


#Entrada
n = int(input("Ingrese el valor: "))

#Procesamiento
x= calcular_tabla(n)
#Salida
print(f"\n La tabla de: {n}")
print("\nEso era...")