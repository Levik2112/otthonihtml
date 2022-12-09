import random
vezeteknev=["Nagy","Kovács","Tóth","Szabo","Horváth","Varga","Kiss","Molnár","Németh","Balogh","Farkas","Papp","Takács","Juhász ","Mészáros","Simon","Rácz","Fekete","Szilágyi","Török","Fehér","Dobi","Gál"]
keresztnev=["Levente","László","Kristóf","Tamás","Bence","Sándor","Gábor","Márk","Dominik","Olivér","Iván","Dávid","András","Mátyás","Róbert","Róbert","Ádám","Péter","Dániel","Ákos","Ferenc","Marcell","Balázs"]

szazalek=[1,2,3,4,5]
for i in range(100):
    szazalek2=random.choice(szazalek)

    if szazalek2==2:
        print(random.choice(vezeteknev),random.choice(keresztnev),random.choice(keresztnev))
    if szazalek2 != 2:
        print(random.choice(vezeteknev),random.choice(keresztnev))
    
print()

vezeteknev2=["Nagy","Kovács","Tóth","Szabo","Horváth","Varga","Kiss","Molnár","Németh","Balogh","Farkas","Papp","Takács","Juhász ","Mészáros","Simon","Rácz","Fekete","Szilágyi","Török","Fehér","Dobi","Gál"]
keresztnev2=["Hanna","Anna","Jázmin","Luca","Emma","Nóra","Lili","Zsófia","Csenge","Dóra","Réka","Viktória","Rebeka","Fanni","Dorina","Léna","Sára","Vivien","Petra","Lara","Alexandra","Fruzsina","Virág"]

for i in range(100):
    szazalek2=random.choice(szazalek)
    if szazalek2==2:
        print(random.choice(vezeteknev2),random.choice(keresztnev2),random.choice(keresztnev2))
    if szazalek2 != 2:
        print(random.choice(vezeteknev2),random.choice(keresztnev2))
