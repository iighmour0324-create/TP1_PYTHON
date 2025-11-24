
class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        """Retourne la valeur totale du stock pour cet article"""
        return self.prix_ht * self.stock

    def approvisionner(self, qte: int):
        """Augmente le stock et journalise l'opération"""
        self.stock += qte
        with open("mouvements.log", "a", encoding="utf-8") as f:
            f.write(f"Approvisionnement {qte} unités de {self.reference} — Nouveau stock : {self.stock}\n")

    def __str__(self) -> str:
        return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht:.2f} € HT"





articles = [
    Article("A001", "Stylo", 1.5, 100),
    Article("A002", "Cahier", 2.3, 50),
    Article("A003", "Classeur", 5.0, 20)
]

for a in articles:
    print(a)


total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} €")

articles[0].approvisionner(20)
articles[1].approvisionner(30)

print("\nApres approvisionnement :")
for a in articles:
    print(a)
