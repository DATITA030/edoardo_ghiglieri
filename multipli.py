#metodo mio
print ('inserisci il numero per sapere se è divisibile')
numero_inserito = int(input())

for n in range (1, 11):
    print (n) #volendo si può togliere il print di tuuti gli 'n'
    if (numero_inserito/n) == int(numero_inserito/n) :
        print ('è divisibile per', n)
print ()

#metodo di sabrina
print ('inserisci il numero per sapere se è divisibile')
numero_inserito = int(input())

for n in range (2, 10):
    print (n) #volendo si può togliere il print di tuuti gli 'n'
    if numero_inserito % n == 0:
        print ('è divisibile per', n)
print ()

#