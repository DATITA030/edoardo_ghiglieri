
surname = input('inserisci Cognome: ').upper().strip() #.replace(' ','')
name = input('inserisci Nome: ').upper().strip() #.replace(' ','')
sesso = input('inserisci il tuo sesso: M o F ').upper().strip()
day_born = input('inserisci giorno di nascita "GG": ').strip()
month_born = input('inserisci mese di nascita: ').upper().strip()
year_born = input('inserisci anno di nascita "YYYY": ').strip()
luogo_di_nascita = input('inserisci il tuo comune di nascita: ').upper().strip()

tabella_mesi1 = {'GENNAIO':'A', 'FEBBRAIO':'B', 'MARZO':'C', 'APRILE':'D', 'MAGGIO':'E', 'GIUGNO':'H', 'LUGLIO':'L', 'AGOSTO':'M', 'SETTEMBRE':'P', 'OTTOBRE':'R', 'NOVEMBRE':'S', 'DICEMBRE':'T'}
tabella_mesi2 = {'01':'A', '02':'B', '03':'C', '04':'D', '05':'E', '06':'H', '07':'L', '08':'M', '09':'P', '10':'R', '11':'S', '12':'T'}

tabella_nascita = {'MILANO' : 'F205', 'ROMA' : 'H501'}

caratteri_pari = {'0':	'0',	'9':	'9',	'I':	'8',	'R':	'17', '1':	'1',	'A':	'0',	'J':	'9',	'S':	'18', '2':	'2',	'B':	'1',	'K':	'10',	'T':	'19', '3':	'3',	'C':	'2',	'L':	'11',	'U':	'20', '4':	'4',	'D':	'3',	'M':	'12',	'V':	'21', '5':	'5',	'E':	'4',	'N':	'13',	'W':	'22', '6':	'6',	'F':	'5',	'O':	'14',	'X':	'23', '7':	'7',	'G':	'6',	'P':	'15',	'Y':	'24', '8':	'8',	'H':	'7',	'Q':	'16',	'Z':	'25'}
lista_caratteri_pari = list(caratteri_pari.keys())
lista_valori_pari = list(caratteri_pari.values())

caratteri_dispari ={'0':	'1',	'9':	'21',	'I':	'19',	'R':	'8', '1':	'0',	'A':	'1',	'J':	'21',	'S':	'12', '2':	'5',	'B':	'0',	'K':	'2',	'T':	'14', '3':	'7',	'C':	'5',	'L':	'4',	'U':	'16', '4':	'9',	'D':	'7',	'M':	'18',	'V':	'10', '5':	'13',	'E':	'9',	'N':	'20',	'W':	'22', '6':	'15',	'F':	'13',	'O':	'11',	'X':	'25', '7':	'17',	'G':	'15',	'P':	'3',	'Y':	'24', '8':	'19',	'H':	'17',	'Q':	'6',	'Z':	'23'}
lista_caratteri_dispari = list(caratteri_dispari.keys())
lista_valori_dispari = list(caratteri_dispari.values())

conversione_numerica = {'0':	'A',	'13':	'N','1':	'B',	'14':	'O','2':	'C',	'15':	'P','3':	'D',	'16':	'Q','4':	'E',	'17':	'R','5':	'F',	'18':	'S','6':	'G',	'19':	'T','7':	'H',	'20':	'U','8':	'I',	'21':	'V','9':	'J',	'22':	'W','10':	'K',	'23':	'X','11':	'L',	'24':	'Y','12':	'M',	'25':	'Z',}
lista_conversione_numerica = list(conversione_numerica.keys())
lista_conversione_numerica1 = list(conversione_numerica.values())

lista_surname = surname
lista_name = name
print (surname)
print (name)
print (sesso)
print (day_born)
print (month_born)
print (year_born)
print (luogo_di_nascita)

codice_fiscale = []
contatore = 0

#codice cognome

for i in range (0, len(lista_surname)):
    if lista_surname[i] != 'A' and lista_surname[i] != 'E' and lista_surname[i] != 'I' and lista_surname[i] != 'O' and lista_surname[i] != 'U' and lista_surname[i] != ' ':
        codice_fiscale.append(lista_surname[i])
        if len(codice_fiscale) > 2:
            break
    else:
        pass
for i in range(0, len(lista_surname)):
    if lista_surname[i] == 'A' or lista_surname[i] == 'E' or lista_surname[i] == 'I' or lista_surname[i] == 'O' or lista_surname[i] == 'U':
        if len(codice_fiscale) > 2:
            break
        else:
            codice_fiscale.append(lista_surname[i])
    else:
        pass

#codice nome

for i in range(0, len(lista_name)):
    if lista_name[i] != 'A' and lista_name[i] != 'E' and lista_name[i] != 'I' and lista_name[i] != 'O' and lista_name[i] != 'U'and lista_surname[i] != ' ':
        codice_fiscale.append(lista_name[i])
        if len(codice_fiscale) > 5:
            break
    else:
        pass
for i in range(0, len(lista_name)):
    if lista_name[i] == 'A' or lista_name[i] == 'E' or lista_name[i] == 'I' or lista_name[i] == 'O' or lista_name[i] == 'U':
        if len(codice_fiscale) > 5:
            break
        else:
            codice_fiscale.append(lista_name[i])
    else:
        pass

#codice anno

codice_fiscale.append(year_born[2])
codice_fiscale.append(year_born[3])

#codice mese di nascita

if month_born.isdigit() == True:

    for chiave, valore in tabella_mesi2.items():
        mese = (list(tabella_mesi2.keys())[contatore])
        lettera_mese = (list(tabella_mesi2.values())[contatore])
        contatore = contatore + 1

        if month_born == mese:
            codice_fiscale.append(lettera_mese)
            break
        else:
            pass
else:
    for chiave, valore in tabella_mesi1.items():
        mese = (list(tabella_mesi1.keys())[contatore])
        lettera_mese = (list(tabella_mesi1.values())[contatore])
        contatore = contatore + 1

        if month_born == mese:
            codice_fiscale.append(lettera_mese)
            break
        else:
            pass


#codice sesso, giorno di nascita

if sesso != 'M':
    day_born = int(day_born) + 40
    female_dai_born = str(day_born)
    codice_fiscale.append(female_dai_born[0])
    codice_fiscale.append(female_dai_born[1])
else:
    codice_fiscale.append(day_born[0])
    codice_fiscale.append(day_born[1])

#comune di nascita
contatore2 = 0
for chiave, valore in tabella_nascita.items():
    comune = list(tabella_nascita.keys())[contatore2]
    codice_comune = list(tabella_nascita.values())[contatore2]
    contatore2 = contatore2 + 1
    if luogo_di_nascita == comune:
        codice_fiscale.append(codice_comune[0])
        codice_fiscale.append(codice_comune[1])
        codice_fiscale.append(codice_comune[2])
        codice_fiscale.append(codice_comune[3])

somma_pari = 0
for i in range (0, len(codice_fiscale)):
    #print ('1')
    for n in range (0, len(lista_caratteri_pari)):
        if codice_fiscale[i] == lista_caratteri_pari[n] and i%2 != 0:
            somma = int(lista_valori_pari[n])
            somma_pari = somma_pari + somma
            #print('pari',somma)
        else:
            pass
somma_dispari = 0
for i in range (0, len(codice_fiscale)):
    #print('1')
    #print (codice_fiscale[i])
    for n in range (0, len(lista_caratteri_dispari)):
        if codice_fiscale[i] == lista_caratteri_dispari[n] and i%2 == 0 :
            somma2 = int(lista_valori_dispari[n])
            somma_dispari = somma_dispari + somma2
            #print('dispari',somma2)
        else:
            pass

somma_tot = str((somma_pari + somma_dispari)%26)

contatore3 = 0
for chiave,valore in conversione_numerica.items():

    if somma_tot == lista_conversione_numerica[contatore3]:
        codice_fiscale.append(lista_conversione_numerica1[contatore3])
        break
    else:
        if len(codice_fiscale) < 16:
            contatore3 = contatore3 + 1
            pass
        else:
            break






print(' '.join(codice_fiscale))







'''for i in range (0, len(lista_surname)):
    if lista_surname[i] != 'I':
        print('non una i')
    else:
        print ('era una i')'''