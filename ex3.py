
class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initiale(self) -> str:
        """Retourne la première lettre du nom en majuscule"""
        return self.nom[0].upper()

    def __str__(self) -> str:
        return f"{self.nom} — {self.telephone} — {self.email}"



class Carnet:
    def __init__(self):
        self._contacts = []

    def ajouter(self, contact: Contact):
        self._contacts.append(contact)

    def recherche(self, fragment: str):
        """Retourne une liste de contacts dont le nom contient le fragment (insensible à la casse)"""
        fragment = fragment.lower()
        return [c for c in self._contacts if fragment in c.nom.lower()]

    def afficher_tous(self):
        for contact in self._contacts:
            print(contact)

    @property
    def nombre_contacts(self) -> int:
        """Nombre de contacts dans le carnet (lecture seule)"""
        return len(self._contacts)


if __name__ == "__main__":
    c = Carnet()
    c.ajouter(Contact("ighmour imad", "0612345678", "imad@example.com"))
    c.ajouter(Contact("yassin aezmo", "0699988877", "yassinf@example.com"))
    c.ajouter(Contact("samad", "0677001122", "samad@example.com"))

    print("Tous les contacts :")
    c.afficher_tous()

    print("\nRecherche de 'sa' :")
    resultat = c.recherche("sa")
    for contact in resultat:
        print(contact.nom, contact.telephone)

    print("\nNombre total de contacts :", c.nombre_contacts)

    
    print("\nInitiales des contacts :")
    for contact in c._contacts:
        print(contact.nom, "=>", contact.initiale)
