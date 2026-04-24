p = Prix = float(input("Entrez le prix : "))
if p > 30000 :
     print(f"Le prix de votre produit est de {p} , vous devez payer une reduiction de 30% de taxe soit {p*(-0.3)} .")
elif p > 30000 :
     print(f"Le prix de votre produit est de {p} , vous devez payer une majoration  de 30% de taxe soit {p*(0.3)} .")
else:
         print(f"Le prix de votre produit est de {p} , vous ne beneficiez d'aucune reduiction ni majoration .")