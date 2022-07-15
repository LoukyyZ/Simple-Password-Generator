import random

#caractere
lettre = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombre = "123456789"
symboles = "§£$%@#{}[]()!?"
caractere = lettre + lettre.lower() + nombre + symboles
caractere_no_symbols = lettre + lettre.lower() + nombre


while True:
    longeurmdp = int(input("Entrez la longeur du mot de passe / Enter password length :"))
    nombredemdp = int(input("Entrez le nombre de mot de passe a afficher / Enter the number of passwords to display :"))
    caractere_speciaux_ask = str(input("Dois-je mettre des caracteres spéciaux dans le mot de passe / Do I have to put special characters in the password ?:"))
     
    if caractere_speciaux_ask == 'y':
        for i in range(0,nombredemdp):
            mdp = ""
            for i in range(0,longeurmdp):
                cmdp = random.choice(caractere)
                mdp = mdp +cmdp
            print('Votre mot de passe est / Your password is :', mdp)

    elif caractere_speciaux_ask == 'n':
        for i in range(0,nombredemdp):
            mdp = ""
            for i in range(0,longeurmdp):
                cmdp = random.choice(caractere_no_symbols)
                mdp = mdp +cmdp
            print('Votre mot de passe est :', mdp)
    elif caractere_speciaux_ask !='oui' or 'non':
        print ("ERREUR")
            
      
