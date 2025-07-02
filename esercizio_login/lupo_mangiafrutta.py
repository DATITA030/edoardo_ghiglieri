'''•AttributeError : l'attributo passato al metodo è di tipo sbagliato
•IndexError : nella collezione non esiste l'indice richiesto
•KeyError : nel dizionario non c'è la chiave richiesta
•ModuleNotFoundError : il modulo importato non esiste
•NameError : la variabile richiesta non esiste
•SyntaxError : c'è un errore di sintassi nel codice
•TypeError : istruzione applicata al tipo di dato sbagliato
•ValueError : istruzione applicata ad un valore non valido
•ZeroDivisionError : divisione per zero'''

frutti = [
    "mela",
    "banana",
    "arancia",
    "pera",
    "kiwi",
    "ananas",
    "fragola",
    "uva",
    "ciliegia",
    "limone"]


fruit = input("inserisci un frutto: ").strip()
print(fruit) #debug
try:
    for frutto in frutti:
        if fruit == frutto:
            print ('hai vinto')

except ValueError as ex:
    print(ex)