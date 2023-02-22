from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

import database
from database import Etudiant


# etudiant = Etudiant("Gl062", "mark", "william", "L1", "marc@15")
# etudiant.ajouterEtudiant()

list_mot_pass = database.getpassWord()
list_matricule = database.getMatricule()

# print(list_matricule ,list_mot_pass)


class MainWidget(BoxLayout):
    reponse = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def verifier(self):
        try:
            matricule = self.ids.mat.text
            _pass = self.ids.passt.text

            print(matricule, _pass)

            for mot in list_mot_pass:
                for mat in list_matricule:
                    if mot == _pass and mat == matricule:
                        self.reponse = "Connexion en cours ..."
                    else:
                        self.reponse = "information incorrect ..."
        except:
            self.reponse = "veuillez remplir les champs vides"


class BureauVoteApp(App):
    pass


BureauVoteApp().run()
