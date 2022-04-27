class Section:
    def __init__(self,num_section,nom_section,etudiant):
        self.__num_section=num_section
        self.__nom_section = nom_section
        self.__etudiant = etudiant
    def getNumSection(self):
        return self.__num_section
    def getNomSection(self):
        return self.__nom_section
    def getEtudiant(self):
        return self.__etudiant
    # setters