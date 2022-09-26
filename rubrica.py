# Assegnamento 1  aa 2021-22 622AA modulo programmazione 9 crediti
# Gruppo: Arena Biondi
# Alessandro Arena 544907 a.arena11@studenti.unipi.it 3407443572
# Rocco Biondi 546237 r.biondi2@studenti.unipi.it 3393368096
import json
import ast
class Rubrica:
    """ Costruttore: crea una rubrica vuota rappresentata come
        dizionario di contatti vuoto """
    def __init__(self):
        """ crea una nuova rubrica vuota """
        self.rub = {}

    def  __str__(self):
        """ Serializza una rubrica attraverso una stringa
        con opportuna codifica (a scelta dello studente) """
        scelta=True
        while scelta: #Facciamo scegliere all'utente in che modo codificare il dict , se in json o come stringa
            z = input("\n inserisci 1 se vuoi codificare la rubrica in Json altrimenti inserisci 2 se vuoi serializzarla come stringa")
            try: #controlliamo e gestiamo l'eccezione in caso l'utente inserisca un carattere non numerico o differente dalla scelta preposta
                z.isnumeric()==True #attraverso isnumeric() ci accertiamo che il parametro inserito dall'utente sia di tipo numerico
                if int(z) == 1:
                    print(json.dumps(self.rub, indent = 4)) #quì avviene la conversione del json
                    scelta=False
                elif int(z) == 2:
                    print(str(self.rub))
                    scelta=False
                elif int(z) != 1 or int(z) !=2:
                    print("riprova")
                    scelta=True
            except ValueError:
                print("riprova")

    def __eq__(self,r):
        """stabilisce se due rubriche contengono
        esattamente le stesse chiavi con gli stessi dati"""
        if self.rub == r:
            print("Le rubriche hanno le stesse chiavi con gli stessi dati")
        else:
            print("Le rubriche differiscono")


    def __add__(self,r):
        """crea una nuova rubrica unendone due (elimina i duplicati)
        e la restituisce come risultato --
        se ci sono contatti con la stessa chiave nelle due rubriche
        ne riporta uno solo """
        nuovodict=r
        for elemento in self.rub:
            if elemento not in r:
                nuovodict.append(elemento)
        print(r)


    def load(self, nomefile):
        """ carica da file una rubrica eliminando il
        precedente contenuto di self """
        nomefile=open('rubrica_esterna.txt', "r")
        contents = nomefile.read()
        self.rub=ast.literal_eval(contents)
        return(self.rub)
        
    def inserisci(self, nome, cognome, dati):
        """ inserisce un nuovo contatto con chiave (nome,cognome)
        restituisce "True" se l'inserimento è andato a buon fine e "False"
        altrimenti (es chiave replicata) -- case insensitive """
        if nome not in self.rub.keys():
            self.rub[nome+cognome]=dati
            return True
        else:
            return False
        return(self.rub)


    def modifica(self, nome, cognome, newdati):
        """ modifica i dati relativi al contatto con chiave (nome,cognome)
        sostituendole con "newdati" -- restituisce "True" se la modifica
        è stata effettuata e "False" altrimenti (es: la chiave non è presente )"""


    def cancella(self, nome, cognome):
        """ il contatto con chiave (nome,cognome) esiste lo elimina
        insieme ai dati relativi e restituisce True -- altrimenti
        restituisce False """

    def cerca(self, nome, cognome):
        """ restitusce i dati del contatto se la chiave e' presente
        nella rubrica e "None" altrimenti -- case insensitive """

    def store(self, nomefile):
        """ salva su file il contenuto della rubrica secondo
        un opportuno formato (a scelta dello studente)"""
        # il formato da me scelto
        # prevede un contatto per linea
        # nome:cognome:telefono\n

    def ordina(self,crescente=True):
        """ serializza su stringa il contenuto della rubrica come in
            Nannipieri Felice 32255599\n
            Neri Paolo 347555776\n
            Rossi Mario 3478999\n
            Rossi Mario Romualdo 3475599\n
            Tazzini Tazzetti Gianna 33368999\n
            le chiavi ordinate lessicograficamente per Cognome -- Nome
            in modo crescente (True) o decrescente (False)
            Fra nome, cognome e telefono seve essere presente ESATTAMENTE uno spazio
            Restituisce la stringa prodotta """





