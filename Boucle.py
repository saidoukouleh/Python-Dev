# Boucle for
for i in range(10):
    print("Itération", i)

print("--------------------------------------")

for x in range(5):
    print("Bonjour tout le monde !")


x = 0

for i in range(1,50):
    x = x + i
print(f"La somme de 1 à {i} est: {x}")

a = int(input("Entrez un entier: "))
b = 0

for y in range(1, a + 1):
    b = b + y

print(f"La somme de 1 à {y} est: {b}")

# Boucle while
while a < 10:
    print("a est inférieur à 10")
    a += 1
