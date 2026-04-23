# x = int(input("Entrez un entier : "))
# y = float(input("Entrez un nombre"))

# #Division

# if y > 0 :
#     div = x/y
#     print(f"la division de {x} et {y} est : {div}\n")
# else:
#     print("Erreur : Division par zero n'est pas autoriséé. \n")
#     print("vous ne pouvez pas diviser par zero")

# #Modumlo
# if y != 0 :
#     mod = x % y
#     print(f"le modumlo de {x} et {y} est : {mod}\n")
# else:

#     print("y es null")
#     print("vous ne pouvez pas faire le modulo par zero")



nom = input("Quel est votre nom")
Note1 = float(input("Entrez la premiere Note :"))
Note2 = float(input("Entrez la deuxiieme Note :"))
Note3 = float(input("Entrez la Trosieme Note :"))

moy = (Note1 + Note2 + Note3) / 3

if moy >= 10:
    print(f"Felicitation {nom}, vous avez reussi avec une moyenne de {moy:.2f} !")
elif moy>= 7:
     print(f" {nom}, vous ete en zone de rattrapage {moy:.2f} !")
else:
    print(f"FDésole {nom}, vous avez echoué avec une moyenne de {moy:.2f} !")