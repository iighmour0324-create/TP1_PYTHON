class CompteurPage:
    
    total_visites = 0

    def __init__(self, url: str):
        self.url = url
        self.visites_par_page = 0 
        CompteurPage.total_visites += 1

    def afficher_stats(self) -> str:
        return f"Page {self.url} — visites globales : {CompteurPage.total_visites}"

    def enregistrer_lecture(self):
        
        self.visites_par_page += 1


# -------- TEST --------

p1 = CompteurPage("https://example.com/")
p2 = CompteurPage("https://example.com/blog")
p3 = CompteurPage("https://example.com/contact")

for p in (p1, p2, p3):
    print(p.afficher_stats())

print("Total global :", CompteurPage.total_visites)


p1.enregistrer_lecture()
p1.enregistrer_lecture()
p2.enregistrer_lecture()

print("Visites page 1 :", p1.visites_par_page)
print("Visites page 2 :", p2.visites_par_page)
print("Visites page 3 :", p3.visites_par_page)
