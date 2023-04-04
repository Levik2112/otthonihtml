adatok=[]

f=open("EUcsatlakozas.txt")
for e in f:
    adatok.append(e.replace("\n","").split(";"))
f.close()

#print(adatok)

print(f"3. feladat: EU tagállamainak száma: {len(adatok)} db")

csatlakozas2007=0
for csat in adatok:
    #print(csat)
    if "2007" in csat[1]:
        #print(csat)
        csatlakozas2007+=1
#print(csatlakozas2007)        

print(f"4. feladat: 2007-ben {csatlakozas2007} ország csatlakozott.")


for mo in adatok:
    if mo[0]=="Magyarország":
        print(f"5. feladat: Magyaroszág csatlakozásának dátuma: {mo[1]}")

for maj in adatok:
    maj=maj[1].split(".")
    #print(maj)
    if maj[1]=="05":
        print("asd")
