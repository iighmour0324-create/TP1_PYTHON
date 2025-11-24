
class Convertisseur:
    taux_eur_dh = 10.9  
    @staticmethod
    def vers_dh(euros: float) -> float:
        """Convertit des euros en dirhams selon le taux actuel"""
        return euros * Convertisseur.taux_eur_dh

    @classmethod
    def mettre_a_jour_taux(cls, nv_taux: float):
        """Met à jour le taux de conversion"""
        cls.taux_eur_dh = nv_taux

    @staticmethod
    def vers_eur(dirhams: float) -> float:
        """Convertit des dirhams en euros selon le taux actuel"""
        return dirhams / Convertisseur.taux_eur_dh



if __name__ == "__main__":
    montant = 100
    print("Avant mise à jour :", Convertisseur.vers_dh(montant))

    Convertisseur.mettre_a_jour_taux(11.2)
    print("Après mise à jour  :", Convertisseur.vers_dh(montant))


    dirhams = 1120
    print(f"{dirhams} DH = {Convertisseur.vers_eur(dirhams):.2f} €")
