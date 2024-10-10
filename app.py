from math import sqrt 

# função que calcula a hipotenusa de um triângulo retângulo
def calcular_hipotenusa(c1,c2):
    h= sqrt((c1**2)) + ((c2**2))
    return h

# programa principal
print("Calcular Hipotenusa")

# usuario informar os valores dos catetos
c1= float(input("Informe o valor do 1° cateto: ").replace(",","."))
c2= float(input("Informe o valor do 2° cateto: ").replace(",","."))

# Exibe na tela o valor da hipotenusa
print(f"O valor da hipotenusa é {calcular_hipotenusa(c1,c2)}.")