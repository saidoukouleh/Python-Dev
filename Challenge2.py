x = int(input("Entrez un entier : "))
y = float(input("Entrez un nombre : " ))

Opperation = input("Entrez l'operation que vous voulez effectuer : + , - , * , / , % : ")

#Addition
if Opperation == "+" :
    print(f"Le resultat de l'addition de {x} et {y} est : {x+y} .")

#Soustraction
elif Opperation == "-" :
    print(f"Le resultat de la soustraction de {x} et {y} est : {x-y} .")

#Multiplication
elif Opperation == "*" :
    print(f"Le resultat de la multiplication de {x} et {y} est : {x*y} .")

#Division
elif Opperation == "/" :
    print(f"Le resultat de la division de {x} et {y} est : {x/y} .")

#Modulo
elif Opperation == "%" :
    print(f"Le resultat du modulo de {x} et {y} est : {x%y} .")

else:
       print("Vous avez entrer une operation qui n'est pas valide .")
    