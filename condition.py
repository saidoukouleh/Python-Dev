#


Nom = input("Quel est votre Nom :")
Note1 = float(input("Entrez la premiere Note :"))
Note2 = float(input("Entrez la deuxiieme Note :"))
Note3 = float(input("Entrez la Trosieme Note :"))

moy = (Note1 + Note2 + Note3) / 3

if moy >= 10:
    print(f"Felicitation {Nom}, vous avez reussi avec une moyenne de {moy:.2f} !")
elif moy>= 7:
     print(f" {Nom}, vous ete en zone de rattrapage {moy:.2f} !")
else:
    print(f"FDésole {Nom}, vous avez echoué avec une moyenne de {moy:.2f} !")