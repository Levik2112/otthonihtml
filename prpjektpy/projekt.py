#Projekt munka
import sys
import os
#program kezdete   
print("HTML/TXT Fálj készítő V1")
print("-"*30)

def szovKeszito():
        try:
            szovBe = input("Szeretnél létrehozni egy szöveges filet? I/N ")
            print("-"*30)
            if szovBe not in ["I", "N","i","n"]:
                raise ValueError("Nem megfelelő válasz. Az alábbiak közül válassz I/N!")
            if szovBe == "N" or szovBe=="n":
                ujraKerd()
                return
            while True:
                fileNevTxt = input("Mi legyen a file neve? (.txt file formátum!) ")
                if not fileNevTxt.endswith(".txt"):
                    print("A file nevének .txt-re kell végződnie!")
                elif os.path.exists(fileNevTxt):
                    print("A megadott fájlnév már létezik adj meg egy másikat!")
                else:
                    break5
            f = open(fileNevTxt, "w")
            szovegBe = input("A szöveg amit szeretnél bele írni: ")
            print("-"*30)
            f.write(szovegBe)
            f.close()
            print("A szöveges fáljlod készen van!")
            print("-"*30)
            ujraKerd()
        except ValueError as e:
            print(e)

#AZ alap fuggveny
def kerdezes():
    kerdez=input("Szeretnél lértehozni egy HTML filet? I/N ")
    print("-"*30)
    def htmlkeszito():
        
        f=open(fileNev,"w")
        alapStruk="""<html>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HTML</title>
</head>
<body>
<h1>Üdv a HTML fáljlodban.</h1>
\n
</body>
</html>
        """
        f.write(alapStruk)
        f.close()
    if kerdez=="I" or kerdez=="i":
        while True:
            fileNev=input("Mi legyen a HTML file neve?(.html fájl formátum!)")
            print("-"*30)
            if not fileNev.endswith(".html"):
                print("A HTML fájl nevének .html-re kell végződnie!")
            elif os.path.exists(fileNev):
                    print("A megadott fájlnév már létezik adj meg egy másikat!")
            else:
                htmlkeszito()
                print("Alap HTML struktura létrehozva.")
                break
    elif kerdez=="n" or kerdez=="N":
        ujraKerd()
        if ujFile=="N" or ujFile=="n":
            sys.exit()
 
    
    def alapSzoveg():
        with open(fileNev, 'r') as file:
                
            data = file.readlines()
          
            #print(data)
        data[9] = """<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus diam in nibh molestie volutpat. Ut efficitur molestie leo eleifend tincidunt. Aenean nec ante sapien. Donec vehicula tortor elit. Sed sed est quam. Donec consequat nisi non mauris suscipit, in dapibus sapien pharetra. In molestie a ante eget varius. Nulla euismod ligula nec lectus pharetra facilisis. Suspendisse vestibulum, sem sed scelerisque semper, tortor nisl tincidunt mi, nec cursus neque tortor ac sapien. Aliquam tincidunt magna eu ante molestie dictum.    
</p>"""
          
        with open(fileNev, 'w') as file:
            file.writelines(data)
            #print(data)
    def kep():
        
        with open(fileNev, 'r') as file:
            
            data = file.readlines()
      
        data[10] = """<br><img src="peldakep.png" alt="Ha nem jelenik meg a kép"  title="kép leirása "width="150px" height="150px"></br>\n\n"""
      
        with open(fileNev, 'w') as file:
            file.writelines(data)

    def hiperLink():
        with open(fileNev, 'r') as file:
            
            data = file.readlines()
      
        
        data[11] = """\n<a href="peldalink.com">Szöveg</a>\n\n"""
      
        with open(fileNev, 'w') as file:
            file.writelines(data)
    def CssMinta2():
        with open(cssNev, 'r') as file:
            data = file.readlines()
      
            
        
        data[::1]=""
        data="""*
{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: gold;
 
}

body {
background-color: red;
}

h1 {
color: gold;
text-align: left;
text-decoration: overline underline;
text-transform: uppercase;
text-shadow: 2px 2px 5px red;
}"""

        with open(cssNev, 'w') as file:
            file.writelines(data)
    #harmadik css minta atirja a fileban az alapot           
    def CssMinta3():
        
         
        with open(cssNev, 'r') as file:
            data = file.readlines()
      
            
        
        data[::1]=""
        data="""*
{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: black;
 
}

body {
background-color: blue;
}

h1 {
color: black;
text-align: left;
text-decoration: overline underline;
text-transform: uppercase;
text-shadow: 2px 2px 5px red;
}"""
        with open(cssNev, 'w') as file:
            file.writelines(data)
    #negyedik, css minta atirja a fileban az alapot           
    def CssMinta4():
        with open(fileNev, 'r') as file:
            
            data = file.readlines()
            data[::1]=""
            data="""<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Reszponziv Minta</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <div class="box">Minta 1</div>
    <div class="box">Minta 2</div>
    <div class="box">Minta 3</div>
    <div class="box">Minta 4</div>
    <div class="box">Minta 5</div>
    <div class="box">Minta 6</div>
  </div>
</body>
</html>
"""

            data=data.replace("""<link rel="stylesheet" href="styles.css">""","<link rel="+"stylesheet"+" "+"href="+cssNev+">")
            
           
        with open(fileNev, 'w') as file:
            #print(data)
            
            
            file.writelines(data)
            
            

            
        f=open(cssNev,"w")
        adatCSS="""
@media (max-width: 767px) {
    body {
      font-size: 16px;
    }
    .container {
      width: 100%;
      padding: 10px;
    }
    .box {
      width: 100%;
      margin-bottom: 20px;
    }
  }
  
  
  @media (min-width: 768px) and (max-width: 991px) {
    body {
      font-size: 18px;
    }
    .container {
      width: 80%;
      margin: 0 auto;
      padding: 20px;
    }
    .box {
      width: 48%;
      margin-right: 4%;
      margin-bottom: 20px;
      float: left;
    }
  }

  @media (min-width: 992px) {
    body {
      font-size: 20px;
    }
    .container {
      width: 80%;
      margin: 0 auto;
      padding: 40px;
    }
    .box {
      width: 30%;
      margin-right: 5%;
      margin-bottom: 20px;
      float: left;
    }
    .box:nth-child(3n+3) {
      margin-right: 0;
    }
  }
  """
        f.write(adatCSS)
        f.close()
    def CssMinta1():
        with open(cssNev, 'r') as file:
            
            data = file.readlines()
      
            
        
        data[::1]=""
        data="""*
{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: white;
 
}
body {
background-color: black;
}

h1 {
color: white;
text-align: center;
text-decoration: overline underline;
text-transform: uppercase;
text-shadow: 2px 2px 5px red;
}"""
        with open(cssNev, 'w') as file:
            file.writelines(data)
    def CssMinta5():

        with open(cssNev, 'r') as file:
            data=readlines()


            data=""
                
        with open(cssNev, 'w') as file:
            file.writelines(data)
    def css():
        with open(fileNev, 'r') as file:
            data = file.readlines()
      
        
#Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus diam in nibh molestie volutpat. Ut efficitur molestie leo eleifend tincidunt. Aenean nec ante sapien. Donec vehicula tortor elit. Sed sed est quam. Donec consequat nisi non mauris suscipit, in dapibus sapien pharetra. In molestie a ante eget varius. Nulla euismod ligula nec lectus pharetra facilisis. Suspendisse vestibulum, sem sed scelerisque semper, tortor nisl tincidunt mi, nec cursus neque tortor ac sapien. Aliquam tincidunt magna eu ante molestie dictum.    
        data[5] = "<link rel="+"stylesheet"+ " " +"href="+cssNev+">\n</head>\n"
        #print(data[5])
      
        with open(fileNev, 'w') as file:
            file.writelines(data)
            #print(data)
        f=open(cssNev,"w")
        f.write("")
        f.close()
        
   
 
      #ra kerdez a cssre
    kerdezCSS=input("Szeretnél  CSS-t a HTML-ben? I/N ")
    print("-"*30)
    
    
    if kerdezCSS == "I" or kerdezCSS=="i":
        while True:
            cssNev = input("Mi legyen a CSS fájl neve?(.css fájlformátum!) ")
            print("-"*30)
            if not cssNev.endswith('.css'):
                print("A CSS fájl nevének .css-ra kell végződnie!")
            else:
                css()
                print("CSS Link hozzáadva.")
                break  
    elif kerdezCSS=="N" or kerdezCSS=="n":
        print("A HTML-ben nem lesz CSS link alapból")


 

    
    szovKerd=input("Szeretnél egy alap Lorem Ipsumos szöveget a HTML-be? I/N ")
    print("-"*30)
    if szovKerd=="I" or szovKerd=="i":
        alapSzoveg()
        print("Alap szöveg hozzáadva!")
    elif szovKerd=="N" or szovKerd=="n":
        print("Alap szöveg kihagyva!")

     
    

    #kepre kerdez ra
    kerdezKep=input("Szeretnél képet is a HTML-be? I/N ")
    print("-"*30)
    if kerdezKep=="I":
        kep()
        print("Img tag hozzáadva")
    elif kerdezKep=="N" or kerdezKep=="n":
        print("Nem lesz hivatkozás a képre a HTML-ben alapbol!")


   

    #hyperlinkre kerdez ra
    kerdezA=input("Szeretnél egy hyperlinket a HTML-be? I/N ")
    print("-"*30)
    if kerdezA=="I" or kerdezA=="i":
        hiperLink()
        print("Hyperlink hozzáadva!")
    elif kerdezA=="N" or kerdezA=="n":
        print("Hyperlink nem lesz a HTML-be alapbol.")
    #elso css minta 



    #alap css mintára kerdez ra
    if kerdezCSS=="I" or kerdezCSS=="i":
        while True:
                try:
                        
                        kerdezCssMinta=input("Szeretnél előre elkészitett CSS mintákat használni? I/N ")
                        if kerdezCssMinta not in["N","n","I","i"]:
                                raise ValueError("Nem megfelelő válasz. Az alábbiak közül válassz I/N!")
                                print("-"*30)
                        if kerdezCssMinta=="N" or kerdezCssMinta=="n":       
                                print("Csak egy üres CSS lesz a HTML-ed mellé.")
                                break
                        if kerdezCssMinta=="I" or kerdezCssMinta=="i":   
                                minta1=print("1. CSS Minta 1(Fekete alap fehér szöveg)")
                                minta2=print("2. CSS Minta 2(Piros alap arany szöveg)")
                                minta3=print("3. CSS Minta 3(Kék alap fekete szöveg)")
                                minta4=print("4. Reszponziv CSS(Itt nem érvényesek az elöbb hozzáadott dolgok!)")
                                minta5=print("5.Üres CSS")
                                valasztas=input("Valassz egyet az alabbiak kozul: ")
                            #hibakezelés
                                if valasztas=="1":
                                        
                                        CssMinta1()
                                        print("Az első CSS minta hozzáadva.")
                                        break
                                if valasztas=="2":
                                        
                                        CssMinta2()
                                        print("A második CSS minta hozzáadva.")
                                        break
                                if valasztas=="3":
                                        
                                        CssMinta3()
                                        print("A harmadik CSS minta hozzáadva.")
                                        break
                                if valasztas=="4":
                                        
                                        CssMinta4()
                                        print("A negyedik CSS minta hozzáadva.")
                                        break
                                if valasztas=="5:":
                                        
                                        cssMinta5()
                                        print("Az ötödik CSS minta hozzáadva.")
                                        break
                except ValueError as e:
                        print(e)
        

                  

        print("-"*30)
        print("A HTML fileod készen is van!")
        ujraKerd()
def ujraKerd():
    while True:
        try:
            ujFile=input("Szeretnél létrehozni egy másik file-t? I/N ")
            if ujFile not in ["I","N","i","n"]:
                raise ValueError("Nem megfelelő válasz. Az alábbiak közül válassz I/N!")
            break
        except ValueError as e:
            print(e)
        
    if ujFile=="I" or ujFile=="i":
        Bekeres()
    if ujFile=="N" or ujFile=="n":
        print("HTML/Szöveges file készítő, készítette: Dobi Levente, Holczer Mátyás, Lébár Olivér :)")
        sys.exit()
        

            
def Bekeres():
    print("Szia egy HTML-t szeretnél késziteni vagy egy sima szöveges filet?")
    print("1.HTML")
    print("2.Szöveges File")
    while True:
        try:
            beKer = input("Válassz egyet az alábbiak közül: ")
            if beKer not in ["1","2"]:
                raise ValueError("Nem megfelelő válasz. Az alábbiak közül válassz: 1, 2!")
            break
        except ValueError as e:
            print(e)
    if beKer=="1":
        print("HTML-t választottad.")
        print("-"*30)
        kerdezes()

    if beKer=="2":
        print("A szöveges filet választottad.")
        print("-"*30)
        szovKeszito()
while True:
    Bekeres()   
    ujraKerd()
    

