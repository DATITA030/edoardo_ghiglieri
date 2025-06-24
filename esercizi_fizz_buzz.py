#numeri = [int(input('inserisci il primo numero:')),int(input('inserisci secondo numero'))]
#print (numeri)

#primo_numero = int(input('inserisci il primo numero: '))
ultimo_numero = int(input('inserisci l\'ultimo numero: ').strip())
for n in range (1, ultimo_numero+1):
    #print (n) #debug
    if n % 3 == 0 and n % 5 == 0:
        print ('frizz','buzz')
    elif n % 5 == 0:
        print ('buzz')
    elif n % 3 == 0:
        print ('fizz')
    else:
        print (n)

print()

#prova con funzioni
def fizz ():
    print ('fizz')
def buzz ():
    print ('buzz')
def fizz_n_buzz ():
    print ('fizz n bazz')
ultimo_numero = int(input('inserisci l\'ultimo numero: ').strip())
for n in range (1, ultimo_numero+1):
    #print (n) #debug
    if n % 3 == 0 and n % 5 == 0:
        fizz_n_buzz()

    elif n % 5 == 0:
        buzz()
    elif n % 3 == 0:
        fizz()
    else:
        print (n)

print()

#prova con funzione  parametri
def stampa_fizz_buzz (a):
    print (a)

ultimo_numero = int(input('inserisci l\'ultimo numero: ').strip())
for n in range (1, ultimo_numero+1):
    #print (n) #debug
    if n % 3 == 0 and n % 5 == 0:
        stampa_fizz_buzz('fizz n buzz')
    elif n % 5 == 0:
        stampa_fizz_buzz('fizz')
    elif n % 3 == 0:
        stampa_fizz_buzz('buzz')
    else:
        print(n)