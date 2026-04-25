# Boucle for
for i in range(10):
    print("Itération", i)

print("--------------------------------------")

for x in range(5):
    print("Bonjour tout le monde !")

print("--------------------------------------")
x = 0

for i in range(1,50):
    x = x + i
print(f"La somme de 1 à {i} est: {x}")

a = int(input("Entrez un entier: "))
b = 0

for y in range(1, a + 1):
    b = b + y

print(f"La somme de 1 à {y} est: {b}")

print("--------------------------------------")
#compter les nombre de lettres dans une chaîne et afficher lettre par letrre
nom = input("Entrez un nom: ")
for x in range(len(nom)):
 print(nom[x])

print("--------------------------------------")

# le nom par escalier
for i in range(len(nom)):
    print(nom[:i+1])

print("--------------------------------------")

# Afficher le nom par inverse
for i in range(len(nom)):
    print(nom[::-1])

    #Aficher le nom en carre
for i in range(len(nom)):
    print(nom*4)

print("--------------------------------------")
# Afficher un nom chaine de caractère par caractère deux deux
for i in range(0, len(nom), 2):
    print(nom[i], end='')

print("--------------------------------------")

t= 0
for i in range(len(nom)):
    if nom[i] != " ":
        t += 1
print(f"Le nombre de lettres dans le nom est: {t}")