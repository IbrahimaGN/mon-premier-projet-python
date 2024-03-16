import csv  # Importation du module csv pour la manipulation des fichiers CSV
from datetime import datetime  # Importation de la classe datetime du module datetime pour la manipulation des dates
import re  # Importation du module re pour l'utilisation des expressions régulières
from tabulate import tabulate

# Regex pour le numéro
regex_numero = r'^[A-Z0-9]{7}$'  # Expression régulière pour le numéro au format spécifié
# Regex pour le prénom
regex_nom = r'^[A-Za-z].*[A-Za-z].*[A-Za-z].*$'  # Expression régulière pour le prénom au format spécifié
# Regex pour le nom
regex_prenom = r'^[A-Za-z].*[A-Za-z].*$'  # Expression régulière pour le nom au format spécifié
# Regex pour la classe (après conversion)
regex_classe = r'^[3-6]e[ABCD]$'  # Expression régulière pour la classe au format spécifié
#expression regulière pour les notes
regex_note=r'([A-Za-z]+)\[([^:]+):([^\]]+)\]'
# Définition du nom du fichier
filename = "Donnees_Projet_Python_Dev_Data.csv"  # Nom du fichier CSV à traiter
# Fonction pour convertir une date au format DD/MM/AA
def convertir_date(date_str):
    date_formats = ['%d/%m/%Y', '%d-%m-%Y', '%d %m %Y','%d,%m,%Y', '%d:%m:%Y', '%d/%m/%y', '%d-%m-%y', '%d %m %y', '%d,%m,%y', '%d:%m:%y',
        '%d.%m.%y', '%d.%m.%Y', '%d|%m|%Y', '%d,%B,%y', '%d/%B/%y', '%d_%m_%Y', '%d_%m_%y']
    for fmt in date_formats:
        date_str=date_str.replace("                        1 fev 2004","01 02 2004")
        date_str=date_str.replace("decembre","12")
        date_str=date_str.replace("mars","03")
        try:
            date=datetime.strptime(date_str, fmt).strftime('%d/%m/%y')
            return date
        except ValueError:
            continue
    return False
# Fonction pour convertir la classe
def convertir_classe(classe_str):
    # Vérification si la chaîne est vide
    if not classe_str:
        return classe_str  # Renvoyer la chaîne vide telle quelle
    # Remplacement des différentes orthographes
    if "ieme" in classe_str:
        classe_str = classe_str.replace("ieme", "e")
    elif "ièm" in classe_str:
        classe_str = classe_str.replace("ièm", "e")
    elif "iem" in classe_str:
        classe_str = classe_str.replace("iem", "e")
    elif "eme" in classe_str:
        classe_str = classe_str.replace("eme", "e")
    elif "em" in classe_str:
        classe_str = classe_str.replace("em", "e")
    elif "ème" in classe_str:
        classe_str = classe_str.replace("ème", "e")
    elif "ie" in classe_str:
        classe_str = classe_str.replace("ie", "e")
    elif " " in classe_str:
        classe_str = classe_str.replace(" ", "")

    # Suppression des espaces et mise en majuscule
    classe_str = classe_str.replace(" ", "").upper()

    # Vérification si la chaîne est vide après les remplacements
    if not classe_str:
        return classe_str  # Renvoyer la chaîne vide telle quelle

    # Mise en majuscule de la lettre de la classe
    classe_str = classe_str[:-1].lower() + classe_str[-1]
    return classe_str

# Fonction pour extraire les notes
def extraire_notes(chaine_notes):
    resultats = {}  # Dictionnaire pour stocker les résultats des notes
    matieres = chaine_notes.split("#")  # Séparation des matières par '#'
    for matiere in matieres:  # Boucle sur chaque matière
        correspondance = re.match(r'([A-Za-z]+)\[([^:]+):([^\]]+)\]', matiere)  # Recherche d'un motif correspondant à la structure des notes
        if correspondance:  # Si un motif est trouvé
            nom_matiere, devoirs_str, examen_str = correspondance.groups()  # Récupération des groupes capturés dans le motif
            try:
                # Conversion des virgules en points pour les notes de devoirs
                notes_devoir = [float(note.replace(",", ".")) for note in re.findall(r'-?\d+[\.,]?\d*', devoirs_str)]
                # Conversion des virgules en points pour la note d'examen
                note_examen = float(examen_str.replace(",", "."))

                # Vérifier si la liste notes_devoir est vide
                if not notes_devoir:
                    raise ValueError("Aucune note de devoir trouvée.")

                # Calcul de la moyenne
                moyenne = ((sum(notes_devoir)/len(notes_devoir)) + 2 * note_examen) / 3
                moyenne_arrondie = round(moyenne, 2)  # Arrondir la moyenne à 2 chiffres après la virgule

                # Ajout des résultats dans le dictionnaire resultats
                resultats[nom_matiere.strip()] = [notes_devoir,note_examen,moyenne_arrondie]
            except ValueError as e:  # Gestion des erreurs de conversion
                print(f"Ignoré: {e}")
            except Exception as e:  # Gestion des autres erreurs
                print(f"Une erreur s'est produite : {e}")

    # Calcul de la moyenne générale
    if resultats:
        moyenne_generale = sum(resultats[matiere][2] for matiere in resultats) / len(resultats)
        moyenne_generale_arrondie = round(moyenne_generale, 2)  # Arrondir la moyenne à 2 chiffres après la virgule
        resultats["Moyenne générale"] = moyenne_generale_arrondie
        resultats=moyenne_generale_arrondie
    else:
        return None

    return resultats

def validation():
    table_data1=[]
    table_data2=[]
    with open(filename, 'r') as f:  # Ouverture du fichier CSV en lecture
        reader = csv.DictReader(f)  # Création d'un lecteur CSV à partir du fichier
        for row in reader:  # Boucle sur chaque ligne du fichier
            numero = row['Numero']  # Récupération du numéro depuis la ligne courante
            match_numero = re.search(regex_numero, numero)  # Recherche du numéro dans la chaîne
            numero = match_numero.group(0) if match_numero else False  # Si un numéro est trouvé, l'extraire, sinon, mettre le numéro de la ligne courante
            nom = row['Nom']  # Récupération du nom depuis la ligne courante
            match_nom=re.search(regex_nom, nom)  # Recherche du nom dans la chaîne
            nom=match_nom.group(0) if match_nom else False # Si un nom est trouvé, l'extraire, sinon, mettre le nom de la ligne courante
            prenom = row['Prénom']  # Récupération du prénom depuis la ligne courante
            match_prenom=re.search(regex_prenom, prenom)   # Recherche du prénom dans la chaîne
            prenom=match_prenom.group(0) if match_prenom else False  # Si un prénom est trouvé, l'extraire, sinon, mettre le prénom de la ligne courante
            date_naissance = row['Date de naissance']  # Récupération de la date de naissance depuis la ligne courante
            date_naissance_convertie = convertir_date(date_naissance)  # Conversion de la date de naissance
            classe = row['Classe']  # Récupération de la classe depuis la ligne courante
            classe_convertie = convertir_classe(classe)  # Conversion de la classe
            match_classe= re.search(regex_classe, classe_convertie)   # Recherche de la classe dans la chaîne
            Classe=match_classe.group(0) if match_classe else False   # Si une classe est trouvée, l'extraire, sinon, mettre la classe de la ligne courante
            note=row['Note']  # Récupération des notes depuis la ligne courante
            resultats=extraire_notes(note)  # Extraction des notes de la ligne courante
            match_note=re.search(regex_note,note)
            Note=match_note.group(0) if match_note else False
            # Ajouter une nouvelle ligne de données à table_data1 ou table_data2
            if match_numero and match_nom and match_prenom and date_naissance_convertie!=False and match_classe and match_note:
                table_data1.append([numero,nom,prenom,date_naissance_convertie,Classe,resultats])  # Ajout à table_data1 si les données sont valides
            else:
                table_data2.append([numero,nom,prenom,date_naissance_convertie,Classe,resultats])  # Ajout à table_data2 si les données sont invalides
    return table_data1, table_data2

def donnees_valides():
    table_data1, _ = validation()
    # Afficher les données valides avec tabulate
    headers = ["Numéro", "Nom", "Prénom", "Date_Naissance", "Classe","Moyenne générale"]
    print(tabulate(table_data1, headers=headers, tablefmt="grid"))

def donnees_invalides():
    _, table_data2 = validation()
    # Afficher les données invalides avec tabulate
    headers = ["Numéro", "Nom", "Prénom", "Date_Naissance", "Classe","Moyenne générale"]
    print(tabulate(table_data2, headers=headers, tablefmt="grid"))

def afficher_par_numero():
    resultat=[]
    numero=input("Veuillez entrer le numéro  :")
    with open(filename, 'r') as f:  # Ouverture du fichier CSV en lecture
        reader = csv.DictReader(f)  # Création d'un lecteur CSV à partir du fichier
        for row in reader:  # Boucle sur chaque ligne du fichier

            if row['Numero']==numero :
                resultat.append(row)
                #print(resultat)
        
    print(tabulate(resultat, tablefmt="grid"))

def afficher_5_premiers():
    table_data1, _ = validation()
    table_data1.sort(key=lambda x: x[5], reverse=True)
    print("Les 5 premiers élèves :\n")
    headers = ["Numéro", "Nom", "Prénom", "Date_Naissance", "Classe", "Moyenne générale"]
    print(tabulate(table_data1[:5], headers=headers, tablefmt="grid"))

def saisir_eleve() :
    Code=input("Entrez votre code  :")
    Numero=input("Entrez son numero :")
    Nom=input ("Entrez son nom :")
    Prenom=input("Entrez son prénom :")
    Date_naissance=input("Entrez sa date de naissance :")
    Classe=input("Entrez sa classe :")
    Note=input("Entrez ses notes (matières[devoir|devoir:examen #...) :")

    return Code,Numero,Nom,Prenom,Date_naissance,Classe,Note

def ajouter_eleve ():
    Code,Numero,Nom,Prenom,Date_naissance,Classe,Note=saisir_eleve()
    nouvel_eleve=[Code,Numero,Nom,Prenom,Date_naissance,Classe,Note]
    with open(filename, 'a',newline="") as f:  # Ouverture du fichier CSV en lecture
        writer = csv.writer(f)  # Création d'un lecteur CSV à partir du fichier
        writer.writerow(nouvel_eleve)
        eleve=nouvel_eleve
    return eleve

def modifier_information():
    numero_ligne = input("Entrez le numéro de la ligne à modifier : ")

    # Charger le contenu du fichier CSV dans une liste de dictionnaires
    with open(filename, 'r', newline="") as f:
        reader = csv.DictReader(f)
        donnees = list(reader)

    # Rechercher la ligne à modifier
    for donnee in donnees:
        if donnee['Numero'] == numero_ligne:
            print("Ligne à modifier :")
            print(donnee)
            colonne_modif = input("Entrez le nom de la colonne à modifier : ")
            nouvelle_valeur = input("Entrez la nouvelle valeur : ")
            donnee[colonne_modif] = nouvelle_valeur
            break
    else:
        print("Numéro de ligne non trouvé.")
        return

    # Réécrire tout le contenu du fichier CSV avec les modifications
    with open(filename, 'w', newline="") as f:
        fieldnames = donnees[0].keys()  # Utiliser les clés du premier dictionnaire pour les en-têtes
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(donnees)

def afficher_page_de_5(nom_fichier, numero_page):
    lignes_par_page = 5
    debut = (numero_page - 1) * lignes_par_page
    fin = debut + lignes_par_page
    
    with open(nom_fichier, newline='') as csvfile:
        lecteur = csv.reader(csvfile)
        lignes = list(lecteur)
        page = lignes[debut:fin]
        for ligne in page:
            print(ligne)

def afficher_page_personnalise(filename, numero_page, lignes_par_page):
    with open(filename, newline='') as csvfile:
        lecteur = csv.reader(csvfile)
        lignes = list(lecteur)
        debut = (numero_page - 1) * lignes_par_page
        fin = debut + lignes_par_page
        page = lignes[debut:fin]
        for ligne in page:
            print(ligne)