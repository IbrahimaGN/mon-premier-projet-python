from FonctionApp import *

#menu numero 1
def menu_1():
    while True:
        try:
            print("Menu 1")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("1.Afficher les informations (valides ou invalides)")
            print("2.Afficher les informations par son numero")
            print("3.Afficher les 5 premiers élèves")
            print("4.Ajouter une information en verifiant sa validité")
            print("5.Modifier une informations ensuite le tranférer dans la structure des informations valides")
            print("6.Quitter")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        
            choix = int(input("Entrez votre choix : "))
            if choix == 1:
                while True:
                    valide = input("Afficher les informations Valides (V) ou Invalides (I) : ")
                    if valide == 'V':
                        donnees_valides()
                        break
                    elif valide == 'I':
                        donnees_invalides()
                        break
                    else:
                        print("Choix invalide. Réessayez :")
            elif choix == 2:
                afficher_par_numero()
            elif choix == 3:
                
                afficher_5_premiers()
            elif choix == 4:
                ajouter_eleve()
            elif choix == 5:
                modifier_information()
            elif choix == 6:
                print("Au revoir !!!!")
                break
            else:
                print("Choix invalide. Réessayez")
        except ValueError:
            print("Choix invalide. Veuillez choisir entre 1 et 5 ou 6 pour quitter")

#menu numero 1
def menu_2():
    while True:
        try:
            print("Menu 2")
            print("::::::::::::::::::::::::::::::::")
            print("::::::::::::::::::::::::::::::::")
            print("1. la pagination par 5 lignes  :")
            print("2. la pagination selon le choix:")           
            print("0. Quittez")
            print("::::::::::::::::::::::::::::::::")
            print("::::::::::::::::::::::::::::::::")

            choix = int(input("Entrez votre choix : "))
            if choix==1 :
                while True:
                    try:
                        # Demander à l'utilisateur le numéro de la page à afficher
                        numero_page = int(input("Entrez le numéro de la page à afficher (0 pour quitter) : "))
                        if numero_page == 0:
                            break
                        afficher_page_de_5(filename, numero_page)
                    except ValueError:
                        print("Veuillez entrer un numéro de page valide.")
            elif choix==2:
                # Demander à l'utilisateur le nombre de lignes par page
                lignes_par_page = int(input("Entrez le nombre de lignes par page : "))
                while True:
                    try:
                        # Demander à l'utilisateur le numéro de la page à afficher
                        numero_page = int(input("Entrez le numéro de la page à afficher (0 pour quitter) : "))
                        if numero_page == 0:
                            break
                        afficher_page_personnalise(filename, numero_page, lignes_par_page)
                    except ValueError:
                        print("Veuillez entrer un numéro de page valide.")
            elif choix==0:
                break
            else:
                print("Choix invalide. Réessayez")
        except ValueError:
            print("Choix invalide. Veuillez choisir entre 1 et 2 ou 0 pour quitter")

#menu principal
def menuPrincipal():
    while True:
        try:
            print("Menu Principal")
            print(":::::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::::")
            print("1. Afficher le menu 1 :")
            print("2. Afficher le menu 2 (la pagination) :")
            print("0.Quittez !!")

            print(":::::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::::")

            choix = int(input("Entrez votre choix : "))
            if choix==1:
                menu_1()
            elif choix==2:
                menu_2()
            elif choix==0:
                exit()
            else:
                print("Choix invalide. Réessayez")
        except ValueError:
            print("Choix invalide. Veuillez choisir entre 1 et 2 ou 0 pour quitter")

#Appel de la fonction menu Principal
menuPrincipal()