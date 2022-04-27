import etudiant
import projet
import section

def creer_liste_etudiants():
    listeetudiant=[]
    return listeetudiant

def creer_liste_projets():
    listeprojet=[]
    return listeprojet

def creer_liste_sections():
    listesection=[]
    return listesection

def afficher_etudiants(listeetudiant):
    for i in range(len(listeetudiant)):
        print("_______________________")
        print("Numéro : ",listeetudiant[i].getNumEtudiant())
        print("Nom: ", listeetudiant[i].getNom())
        print("Prénom: ", listeetudiant[i].getPrenom())
    print("_______________________")

def afficher_projets(listeprojet):
    for i in range(len(listeprojet)):
        print("_______________________")
        print("Numéro Projet: ",listeprojet[i].getNumProjet())
        print("Theme: ", listeprojet[i].getTheme())
    print("_______________________")

def afficher_sections(listesection):
    for i in range(len(listesection)):
        print("_______________________")
        print("Numéro Section: ",listesection[i].getNumSection())
        print("Nom Section: ", listesection[i].getNomSection())
    print("_______________________")

def afficher_projets_etudiants(listeprojet):
    for i in range(len(listeprojet)):
        print("_______________________")
        print("Numéro Projet: ", listeprojet[i].getNumProjet())
        print("Theme: ", listeprojet[i].getTheme())
        if (listeprojet[i].getEtudiant()==None):
            print("Le numéro de l'étudiant est inexistant")
        else:
            print("Numéro étudiant: ",listeprojet[i].getEtudiant().getNumEtudiant())
            print("Nom étudiant: ", listeprojet[i].getEtudiant().getNom())
            print("Prénom étudiant: ", listeprojet[i].getEtudiant().getPrenom())

    print("_______________________")

def afficher_sections_etudiants(listesection):
    for i in range(len(listesection)):
        print("_______________________")
        print("Numéro Section: ", listesection[i].getNumSection())
        print("Nom Section: ", listesection[i].getNomSection())
        if (listesection[i].getEtudiant()==None):
            print("Le numéro de l'étudiant est inexistant")
        else:
            print("Numéro étudiant: ",listesection[i].getEtudiant().getNumEtudiant())
            print("Nom étudiant: ", listesection[i].getEtudiant().getNom())
            print("Prénom étudiant: ", listesection[i].getEtudiant().getPrenom())

    print("_______________________")

def main():
    choix = 0
    listeetudiant=creer_liste_etudiants()
    listeprojet=creer_liste_projets()
    listesection=creer_liste_sections()
    while choix==0:
       print("-----------------------")
       print("1.Créer une section")
       print("2.Créer un projet")
       print("3.Créer un etudiant")
       print("4.Lister les sections")
       print("5.Lister les projets")
       print("6.Lister les etudiants")
       print("7.Afficher les étudiants d'une section donnée")
       print("8.Afficher les étudiants qui travillent dans un projet donné")
       print("9.Afficher pour chaque projet, les étudiants qui y travillent et leurs sections respectives")
       print("10.Sortie")
       print("-----------------------")
       choix=int(input("Votre choix ?"))
       if choix==1:
           mum_section = int(input("Numéro de section?"))
           nom_section = input("Nom section?")
           rep = input("Y a t'il des étudiants dans cette section? (O/N)")
           rep = rep.upper()
           if rep == "N":
               etd = None
               sec = section.Section(mum_section, nom_section, etd)
               listesection.append(sec)
               choix = 0
           else:
               valide = 0
               while valide == 0:
                   num = int(input("Numéro de l'étudiant?"))
                   et = None
                   for i in range(len(listeetudiant)):
                       if (listeetudiant[i].getNumEtudiant()==num):
                           et = listeetudiant[i]
                           break
                   if et==None:
                       valide = 0
                       print("Le numéro de l'étudiant est inexistant")
                   else:
                       valide = 1
                       sec2 = section.Section(num_section, nom_section, et)
                       listesection.append(sec2)
                   choix = 0
       elif choix==2:
           mum_projet = int(input("Numéro du projet?"))
           theme = input("Thème de la section?")
           rep = input("Y a t'il des étudiants assigné à ce projet? (O/N)")
           rep = rep.upper()
           if rep == "N":
               etd = None
               proj = projet.Projet(mum_projet, theme, etd)
               listeprojet.append(proj)
               choix = 0
           else:
               valide = 0
               while valide == 0:
                   num = int(input("Numéro de l'étudiant?"))
                   et = None
                   for i in range(len(listeetudiant)):
                       if (listeetudiant[i].getNumEtudiant() == num):
                           et = listeetudiant[i]
                           break
                   if et == None:
                       valide = 0
                       print("Le numéro de l'étudiant est inexistant")
                   else:
                       valide = 1
                       proj2 = projet.Projet(mum_projet, theme, et)
                       listeprojet.append(proj2)
                   choix = 0
       elif choix==3:
           num_etudiant = input("Numéro Etudiant?")
           nom = input("Nom Etudiant?")
           prenom = input("Prénom Etudiant?")
           etd = etudiant.Etudiant(num_etudiant, nom, prenom)
           listeetudiant.append(etd)
           choix = 0
       elif choix==4:
           afficher_sections(listesection)
           choix=0
       elif choix==5:
           afficher_projets(listeprojet)
           choix=0
       elif choix==6:
           afficher_etudiants(listeetudiant)
           choix=0
       elif choix==7:
           afficher_sections_etudiants(listesection)
           choix=0
       elif choix==8:
           afficher_projets_etudiants(listeprojet)
           choix=0
       elif choix==9:
           afficher_etudiants(listeetudiant)
           choix=0
       elif choix==10:
           break
       else:
           print("choix invalide!!!")
           choix=0
    print("Fin du programme")

main()