
import random

numero_segreto = random.randint(1,100)
#debug linea 5
print (numero_segreto)

numero_scommesso = 0
numero_tentativo = 5
count = 0
while numero_scommesso != numero_segreto:
    numero_scommesso = input('su quale numero scommetteresti?')
    if numero_scommesso.isdigit() == True :
        numero_scommesso = int(numero_scommesso)
    else:
        print ('scelta non valida, ricomincia e inserisci un numero')
        break

    print (f'hai ancora {numero_tentativo} tentativi')
    numero_tentativo -= 1
    if numero_scommesso == numero_segreto :
        print ('hai vinto')
    elif numero_tentativo < 0:
        print ('hai finito i tentativi')
        break
    else:
        print ('hai sbagliato')
        distanza = abs(numero_scommesso - numero_segreto)
        if distanza <= 5:
            print ('fuoco fuoco')
        elif distanza <= 20:
            print ('fuoco')
        else:
            print ('acqua')
