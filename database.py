import sqlite3

con = sqlite3.connect("GestionVote.db")

cur = con.cursor()

requet = "CREATE TABLE IF NOT EXISTS etudiant (" \
         "matricule varchar(6) primary key ," \
         "nom varchar(20) not null," \
         "prenom varchar(20) not null," \
         "niveau varchar(2) not null," \
         "mot_2_pass varchar(12) not null);"

requet_0 = """CREATE TABLE IF NOT EXISTS candidat(
                matricule varchar(5) primary key,
                nom varchar(20) not null,
                prenom varchar(20) not null,
                niveau varchar(2) not null);"""

requet_01 = """CREATE TABLE IF NOT EXISTS bureau(
                matricule varchar(5) not null,
                comptable varchar(20) not null,
                secretaire varchar(20) not null,
                foreign key (matricule) references candidat(matricule));"""

cur.execute(requet)
cur.execute(requet_0)
cur.execute(requet_01)


class Etudiant:
    matricule = ""
    nom = ""
    prenom = ""
    niveau = ""

    def __init__(self, matricule, nom, prenom, niveau, motpass):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.niveau = niveau
        self.motpass = motpass

    def ajouterEtudiant(self):
        requet_2 = "INSERT INTO etudiant VALUES(?,?,?,?,?)"
        val = (self.matricule, self.nom, self.prenom, self.niveau, self.motpass)
        cur.execute(requet_2, val)
        con.commit()



    def rechercherEtudiant(self, nom, matricule):
        if not nom == "":
            requet_3 = "SELECT " + nom + "from etudiant;"
            etudiant_choisi = cur.execute(requet_3)
            con.commit()
            return etudiant_choisi.fetchone()
        else:
            requet_3 = "SELECT " + matricule + "from etudiant;"
            etudiant_choisi = cur.execute(requet_3)
            con.commit()
            return etudiant_choisi.fetchone()

    def getEtudiant(self):
        liste_Etudaint = cur.execute("""SELECT * FROM etudiant;""")
        con.commit()
        for user in liste_Etudaint.fetchall():
            if user == "":
                return False
            else:
                return {
                    "matricule": user[0], "nom": user[1], "prenom": user[2], "niveau": user[3]
                }


class Candidats:
    matricule = ""
    nom = ""
    prenom = ""
    niveau = ""

    def __init__(self, matricule, nom, prenom, niveau):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.niveau = niveau

    def getCandidat(self):
        liste_Etudaint = cur.execute("""SELECT * FROM candidat;""")
        for user in liste_Etudaint.fetchall():
            if user == "":
                return False
            else:
                return {
                    "matricule": user[0], "nom": user[1], "prenom": user[2], "niveau": user[3]
                }


def getpassWord():
    un = cur.execute("select * from etudiant")
    list = []
    for row in un.fetchall():
        list.append(row[4])
    return list


def getMatricule():
    un = cur.execute("select * from etudiant")
    list = []
    for row in un.fetchall():
        list.append(row[0])
    return list