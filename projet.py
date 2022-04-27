class Projet:
    def __init__(self,num_projet,theme,etudiant):
        self.__num_projet=num_projet
        self.__theme = theme
        self.__etudiant = etudiant
    def getNumPojet(self):
        return self.__num_projet
    def getTheme(self):
        return self.__theme
    def getEtudiant(self):
        return self.__etudiant
    # setters