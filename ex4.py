
from math import pi

class Cercle:
    def __init__(self, rayon: float):
        self._rayon = None  
        self.rayon = rayon 

    @property
    def rayon(self) -> float:
        """Retourne le rayon du cercle"""
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        """Définit le rayon avec contrôle de valeur"""
        if valeur <= 0:
            raise ValueError("Le rayon doit être strictement positif.")
        self._rayon = valeur

    @property
    def perimetre(self) -> float:
        """Retourne le périmètre du cercle"""
        return 2 * pi * self._rayon

    @property
    def surface(self) -> float:
        """Retourne la surface du cercle"""
        return pi * self._rayon ** 2

    def agrandir(self, pourcentage: float):
        """Augmente le rayon de x %"""
        if pourcentage < 0:
            raise ValueError("Le pourcentage doit être positif.")
        self._rayon *= 1 + pourcentage / 100



if __name__ == "__main__":
    c = Cercle(3) 
    print("Surface :", c.surface)      

    
    try:
        c.rayon = -5
    except ValueError as e:
        print("Erreur capturée :", e)

   
    c.agrandir(50) 
    print("Nouveau rayon :", c.rayon)
    print("Nouvelle surface :", c.surface)
