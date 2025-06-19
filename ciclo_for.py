word = 'python'
for character in word:
     print (character)
print ()

for n in range (1, 11):
    print (n)
print ()

for n in range (5):
    print (n)
print ()

for n in range (2, 21, 2):
    print (n)
print ()

for numero in range (0, 10):
    if numero == 5:
        print ('interruzione ciclo', numero,)
        break
    print (numero)
print ()

for number in range (10):
    if number == 5:
        print ('skip', number)
        continue
    print (number)
else:
    print('il ciclo for è finito')
print ()

for row in range (10):
    for column in range (10):
        print ('#', end='   ')
    print()

#esercizio tabelline, con inserimento manuale.

print ('inserisci il numero per la tabellina')
numero_inserito = int(input())

for n in range (numero_inserito, numero_inserito*11, numero_inserito):
    print (n)
print ()