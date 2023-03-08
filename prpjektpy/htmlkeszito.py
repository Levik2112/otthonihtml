#Projekt munka

#letrehoz es beleir egy alapot a filebap
def htmlkeszito():
    f=open("index.html","w")
    alapStruk="""<html>

<head>
<title>HTML</title>
</head>
<body>
<h2>Üdv a HTML fáljlodban.</h2>
\n
</body>
</html>
"""
    f.write(alapStruk)

    
    f.close()

    
#program kezdete   
print("HTML Fálj készítő CSS-el V1")
print("-"*30)

#html alap strukturajanak elkeszitese
kerdez=input("Szeretnél egy alap HTML-t létrehozni? I/N ")
if kerdez=="I":
    htmlkeszito()
    print("Alap HTML struktura létrehozva.")
else:
    print("Viszlát!")

#beleir a fileba egy adott helyre
def css():
    with open('index.html', 'r') as file:
        data = file.readlines()
  
 
    data[4] = """<link rel="stylesheet" src="styles.css">\n</head>\n"""
  
    with open('index.html', 'w') as file:
        file.writelines(data)
        
kerdezCSS=input("Szeretnél  CSS-t a HTML-ben? I/N ")

#ra kerdez a cssre
if kerdezCSS=="I":
    css()
    print("CSS Link hozzáadva.")
else:
    print("A HTML-ben nem lesz CSS link alapból")


#beleir a fileba egy adott helyre   
def kep():
    
    with open('index.html', 'r') as file:
        
        data = file.readlines()
  
    data[8] = """<img src="peldakep.png" alt="Ha nem jelenik meg a kép"  title="kép leirása "width="szélesség" height="magasság">\n\n"""
  
    with open('index.html', 'w') as file:
        file.writelines(data)
        

#kepre kerdez ra
kerdezKep=input("Szeretnél képet is a HTML-be? I/N ")
if kerdezKep=="I":
    kep()
    print("Img tag hozzáadva")
else:
    print("Nem lesz hivatkozás a képre a HTML-ben alapbol!")

#beleir a fileba egy adott helyre
def hiperLink():
    with open('index.html', 'r') as file:
        
        data = file.readlines()
  
    
    data[9] = """\n<a href="peldalink.com">Szöveg</a>\n\n"""
  
    with open('index.html', 'w') as file:
        file.writelines(data)
    


#hyperlinkre kerdez ra
kerdezA=input("Szeretnél egy hyperlinket a HTML-be? I/N ")
if kerdezA=="I":
    hiperLink()
    print("Hyperlink hozzáadva!")
else:
    print("Hyperlink nem lesz a HTML-be alapbol.")


#alap css mintára kerdez ra
kerdezCssMinta=input("Szeretnél előre elkészitett CSS mintákat használni? I/N ")
if kerdezCssMinta=="I":
    minta1=print("1. CSS Minta 1")
    minta2=print("2. CSS Minta 2")
    minta3=print("3. CSS Minta 3")
    minta4=print("4. CSS Minta 4")

    valasztas=input("Valassz egyet az alabbiak kozul: ")







