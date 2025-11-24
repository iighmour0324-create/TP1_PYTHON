
from datetime import datetime

class JournalTaches:
    def __enter__(self):
        """Ouvre le fichier journal.txt en mode append et retourne self"""
        self._fichier = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        """Écrit la tâche précédée de la date-heure ISO"""
        date_heure = datetime.now().isoformat()
        self._fichier.write(f"{date_heure} — {tache}\n")

    def lire(self):
        """Lit l'historique du journal dans l'ordre chronologique inverse"""
        try:
            with open("journal.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
            for ligne in reversed(lignes):
                print(ligne.strip())
        except FileNotFoundError:
            print("Le fichier journal.txt n'existe pas.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ferme le fichier"""
        self._fichier.close()



if __name__ == "__main__":
    from time import sleep

    with JournalTaches() as journal:
        journal.enregistrer("Préparer la réunion du projet X")
        sleep(1)
        journal.enregistrer("Faire la revue de code")
        sleep(1)
        journal.enregistrer("Envoyer le rapport hebdomadaire")

    print("\nContenu du journal (ordre inverse) :")
    j = JournalTaches()
    j.lire()
