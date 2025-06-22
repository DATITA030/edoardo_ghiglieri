import random
#numero_randomico1 = random.randint(0,10)
#numero_randomico2 = random.randint(1,10)  TEST INIZIALE, TROPPO LUNGO
#numero_randomico3 = random.randint(1,10)
#numero_randomico4 = random.randint(1,10)
#numero_randomico5 = random.randint(1,10)
#print (numero_randomico1, numero_randomico2, numero_randomico3, numero_randomico4, numero_randomico5) #debug
numeri = [] #[numero_randomico1,numero_randomico2,numero_randomico3,numero_randomico4,numero_randomico5]
for ciclo in range (0,int(input('inserisci il quantitativo di numeri:'))):  #lol ha funzionato, si può inserire come input
    numeri.append (random.randint(0,10))
print (numeri)
max_position = 0
min_position = 0
max_number = numeri[0]
min_number = numeri [0]
for i in range (0,len(numeri)):
    if numeri[i] > max_number:
        max_number = numeri[i]
        max_position = i

print ('il numero maggiore si trova nella posizione:', max_position)
for n in range (0,len(numeri)):
    if numeri[n] < min_number:
        min_number = numeri[n]
        min_position = n

print ('il numero minore si trova nella posizione:', min_position)
#finalmewnte è funzionante...

#secondo esercizio

