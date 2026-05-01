#Boucle while gestion de mot de passe temps de tentative

mot_de_passe = "1234"
tentatives = 0
while tentatives < 3:
    mot_de_passe_saisi = input("Entrez le mot de passe: ")
    if mot_de_passe_saisi == mot_de_passe:
        print("Mot de passe correct. Accès autorisé.")
        break
    else:
        tentatives += 1
        print(f"Mot de passe incorrect. Tentatives restantes: {3 - tentatives}")


# Cofre fort dune banque
code = "2026"
point = 0
while point < 100:
    code_saisi = input("Entrez le code secret: ")
# dire si le code saisir est petit ou long
    if len(code_saisi) < 4:
        print("Code saisir trop court. Veuillez entrer un code à 4 chiffres.")
        continue
    if len(code_saisi) > 4:
        print("Code saisir trop long. Veuillez entrer un code à 4 chiffres.")
        continue
    if code_saisi == code:
        print("Code secret est correct. Coffre fort est ouverte.")
        break
    else:
        point += 20
        print(f"Code incorrect. Tentatives restantes: {100 - point}")





#Le Brsie code (Code Breaker) 
# creer un progrmme qui simule la tentative douverture dun ordinateur securse
#chaque tentative echoué ya une dimunitkon de 25% de la charge de la batterie

code_pc = 1337
charge_batterie = "100"
saisir = 0

while code_pc != saisir and charge_batterie > 0:
    code_saisi = int(input("Entrez le code pour ouvrir l'ordinateur: "))
    if code_saisi != code_pc:
        charge_batterie -= 25

        if charge_batterie < code_pc:
            print(f"code incorrect. essayer un code plus grand.Il vous reste {charge_batterie}% de batterie.")
        else:
            print(f"code incorrect. essayer un code plus petit.Il vous reste {charge_batterie}% de batterie.")
    
    if saisir == code_pc:
            print("Code correct. vous avez reussir a Hacker l'ordinateur ouvert.")
            break
    else:
           print("Code incorrect. Veuillez réessayer.")