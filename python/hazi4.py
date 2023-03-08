import random
l=[]
for i in range(100):
    l.append(random.randint(1000,9999))
l6 = []
for e in l:
    if e % 6 == 0:
        l6.append(e)
    if e % 12 == 0:
        l6.remove(e)
print("Ezek a számok oszthatók 6-al,de 12-vel nem: ",l6)


print()


lmin=[]
for i in range(100):
    lmin.append(random.randint(-9999,-1000))
lmin6 = []
for e in lmin:
    if e % 6 == 0:
        lmin6.append(e)
    if e % 12 == 0:
        lmin6.remove(e)
print("Ezek a negativ számok oszthatók 6-al,de 12-vel nem: ",lmin6)




