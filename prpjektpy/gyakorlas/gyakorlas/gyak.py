#nev=input("Mi a neve? ")
kor=int(input("Hány éves? "))
melo=input("Mit dolgozik? ")
adat=[]
f=open("gyak.txt")
for e in f:
    adat.append(e.replace("\n","").split(" "))
f.close()
print(adat)
class Szemely:
    neve,kora,munkaja=["",0,""]
    def __init__(self,neve,kora,munkaja):
        self.kora=kora
        self.neve=neve
        self.munkaja=munkaja
    def adatok(self):
        print(f"A neve: {self.neve},a munkaja {self.munkaja},a kora pedig {self.kora}")



ember1=Szemely(adat[0][0],kor,melo)
ember1.adatok()
