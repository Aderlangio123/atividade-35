#Ler uma lista de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(1,11):
    nmr = float(input(f"digite o {i} numero:  "))
    numeros.append(nmr)

numeros.reverse()
print(numeros)