#DICTIONNAIRE 
etudiants = []


while True:
    print("===Menu===")
    print("1. Ajouter un etudiant")
    print("2. Afficher les etudiants")
    print("3. Afficher les Admin")
    print("4. Afficher les meuilleurs etudiants")
    print("5. Quitter")
    choix = input("Entree votre choix : ")

    if choix == '1':
        nom = input("Entree le nom de l'etudiant : ")
        age = int(input("Entree l'age de l'etudiant : "))
        note = float(input("Entree la note de l'etudiant : "))

        etudiant = {
        "nom": nom,
        "age": age,
        "note": note
          }
 
        etudiants.append(etudiant)
        print("Etudiant ajoutee avec succes")
    elif choix == '2':
        if len(etudiants) == 0:
            print("Aucun etudiant trouve")  
        else:
            print("===Liste des etudiants===")
            for e in etudiants:
                print(f"Nom : {e['nom']}, Age : {e['age']}, Note : {e['note']}")        
    elif choix == '3':
        print("===Affichage des etudiants admis===")
        for e in etudiants:
            if e['note'] >= 10:
                print(f"Nom : {e['nom']}, Age : {e['age']}, Note : {e['note']}")    
    elif choix == '4':
        print("===Affichage des meuilleurs etudiants===")
        meuilleure_note = 0    
        for e in etudiants:
            if e['note'] > meuilleure_note:
                meuilleure_note = e['note']
                meuilleurçe_etudiant = e['nom']
        print(f"Le meuilleure etudiant est : {meuilleurçe_etudiant} avec une note de {meuilleure_note}")
    elif choix == '5':
        print("QUITTER!") 
        break  
    else:
        print("Choix invalide, AUREVOIR!") 

        
    
