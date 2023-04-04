import random
vers1="""Ól sarkában disznó röfög,meglocsollak, aztán mögyök!"""
vers2="""Zöld erdőben jártam,lejártam a lábam,már mindenem dagad,locsold meg most magad!"""
vers3="""Elég szar volt ez a hetem,ezt a kölnit rád önthetem?"""


versek=[vers1,vers2,vers3]
#print(versek)


class locsolo:
    nev,ft,tojas,palinka,vers=["",0,0,0,""]
    def __init__(self,nev,ft,tojas,palinka,vers):
        self.nev=nev
        self.ft=ft
        self.tojas=tojas
        self.palinka=palinka
        self.vers=vers
        
    def ugat(self):
        print("vau")
    def penz(self):
        print("Ennyi pénzt gyűjtöttem: {}".format(self.ft))
    def tojgli(self):
        print("Ennyi tojást gyűjtöttem: {}".format(self.tojas))
    def pia(self):
        print("Ennyi pálinkát ittam: {}".format(self.palinka))
        
    def bemutatkozik(self):
        print("Szia,üdv {} vagyok!".format(self.nev))
                    
    def szaval(self):
        
        if self.palinka > 5:
            uj_vers = ""
            for i, c in enumerate(self.vers):
                if i % 2 == 0:
                    uj_vers += c.lower()
                else:
                    uj_vers += c.upper()
            self.vers = uj_vers
            
        if self.palinka > 8:
            print("Ez a versem: SAFDSF")
        
        else:
            print("Ez a versem: {}".format(self.vers))

        


ember1=locsolo("Pisti",random.randint(500,5000),random.randint(1,10),random.randint(1,10),random.choice(versek))

ember2=locsolo("Feri",random.randint(500,5000),random.randint(1,10),random.randint(1,10),random.choice(versek))

ember3=locsolo("István",random.randint(500,5000),random.randint(1,10),random.randint(1,10),random.choice(versek))
ember4=locsolo("László",random.randint(500,5000),random.randint(1,10),random.randint(1,10),random.choice(versek))
ember5=locsolo("Levi",random.randint(500,5000),random.randint(1,10),random.randint(1,10),random.choice(versek))

ember1.bemutatkozik()
ember1.pia()
ember1.szaval()
ember1.penz()
ember1.tojgli()
print()
ember2.bemutatkozik()
ember2.pia()
ember2.szaval()
ember2.penz()
ember2.tojgli()
print()
ember3.bemutatkozik()
ember3.pia()
ember3.szaval()
ember3.penz()
ember3.tojgli()
print()
ember4.bemutatkozik()
ember4.pia()
ember4.szaval()
ember4.penz()
ember4.tojgli()
print()
ember5.bemutatkozik()
ember5.pia()
ember5.szaval()
ember5.penz()
ember5.tojgli()

