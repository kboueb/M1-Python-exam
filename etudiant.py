class Etudiant:
    def __init__(self,num_etudiant,nom,prenom):
        self.__num_etudiant=num_etudiant
        self.__nom=nom
        self.__prenom=prenom
    def getNumEtudiant(self):
        return self.__num_etudiant
    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    # définir   aussi les setters