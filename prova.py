#import json
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory2 = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217, 'mele':374}

import ast
#scelta=True
#while scelta: 
#    z = input("\n inserisci 1 se vuoi codificare la rubrica in Json altrimenti inserisci 2 se vuoi serializzarla come stringa")
#    try:
#        z.isnumeric()==True
#        if int(z) == 1:
#            print(json.dumps(inventory, indent = 4))
#            scelta=False
#        elif int(z) == 2:
#            print(str(inventory))
#            scelta=False
#        elif int(z) != 1 or int(z) !=2:
#            print("riprova")
#            scelta=True
#    except ValueError:
#       print("riprova")ù

#def DictListUpdate( lis1, lis2):
#    nuovalista=lis2
 #   for aLis1 in lis1:
  #      if aLis1 not in lis2:
   #         nuovalista.append(aLis1)
    #return nuovalista
#print (DictListUpdate(inventory,inventory2))

nuova_rubrica='rubrica_esterna.txt'
file = open('rubrica_esterna.txt', "r")
contents = file.read()
dictionary = ast.literal_eval(contents)
class prova:
    def __init__(self):
        self.rub={}
    def load(self, nomefile):
            """ carica da file una rubrica eliminando il
            precedente contenuto di self """
            self.rub=nomefile
            return(dict(self.rub))
    def inserisci(self, nome, cognome, dati):
        """ inserisce un nuovo contatto con chiave (nome,cognome)
        restituisce "True" se l'inserimento è andato a buon fine e "False"
        altrimenti (es chiave replicata) -- case insensitive """
        if nome not in self.rub.keys():
            self.rub[nome+cognome]=dati
            return self.rub, "Modifica Eseguita"
        else:
            return False
p=prova()
p.load(dictionary)
print(p.inserisci("sangiovanni ","Felice",32255599))