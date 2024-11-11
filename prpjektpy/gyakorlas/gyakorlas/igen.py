import sys
import time
import socket
import requests
from requests import get
from json import loads



print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PJ7!^^::::::^^!7JP#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J.                  :P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B  .:^^:        :^^^. .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@? ^~!YPGGJ.  :JGGPJ!~^ J@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@~     .~YP:  ~PJ~..    7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@#J&@@@@@@@@@@@@@@@@@&^.?PBBB5!YY  .^75GBBP!.!@@@@@@@@@@@@@@@@@@&P@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@~^G@@@@@@@@@@@@@@@@&^^7!!~~~:YB    ^^^^^^^.!@@@@@@@@@@@@@@@@@G^Y@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#^ !G@@@@@@@@@@@@@@@P.       BG            Y@@@@@@@@@@@@@@@B! 7@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#~  7B@@@@@@@@@@@@@#J?!^^:!5&5   :^ ::^~7?&@@@@@@@@@@@@@#?. ?@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&?  .?B@@@@@@@@@@@@Y?55!:~^5? .. . :7GJJG@@@@@@@@@@@@&J.  Y@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@P^  .7B@@@@@@@@@@@5~5G555#B7Y#PY555Y75@@@@@@@@@@@&Y:  :P@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&?   .7G@@@@@@@@@@G~Y5~~~~:~!!~::~7G@@@@@@@@@@B?:   7#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@B!    ^JB@@@@@@@@#?J^ .!BG:  .^?&@@@@@@@@#5~    ~P@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@B7.   .~5#@@@@@@@P^  Y@#:  ^P@@@@@@@#5!.   .7B@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BJ^    .7P&@@@@@#J:J@B:^Y&@@@@@#5!.    ^J#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P!.  ~!~?P#@@@@&#@&B@@@@@BY7!^   :7P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BY~..~!!!75B&@@@@@&G5?7777~.:?P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@B7!5@@@@@@#5!^^~77!!7YPB5!7??!^:^?G&@@@@@&#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5^ P@@@@@@@&BJ!~^^~!7!!!7YJ7!Y#@@@@@@@@J:.7#@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@#PP&&&&@&!.J#GJ7!~~~!?Y57!~~^^~!!!!!!!7J5GB@@? ^G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&:  P!:::^JY:.^Y57!!~~~~!?5#@#GY7~~~~!!!!7J?J^ 7GPPP5GP7Y&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@P7!5PPPPPG@B  PGPPGB#&@@@@@@@@@@@&#GP5YYY&7 :BP~^^:^Y~  P@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@B&@@@@@@@Y..JPPP&@@@@@@@@@@@@@@@@@&&@&P: 5@@@@@@#555B@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P?!!J&@@@@@@@@@@@@@@@@@?~!~~?G@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
print()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("Jelnlegi idő a program használata közben: "+ current_time)
print()
print("Jelentkezz be a program használatához vagy regisztrálj!!")
print()
print("1.Bejelenkezés")
print("2.Regisztárció")
valasztas=input("Válassz az alábbiak közül: ")
adatok=[]
f=open("adatbazis.txt")
for e in f:
    adatok.append(e.replace("\n",""))
f.close
print(adatok)
if valasztas=="1":
    
    hibak=0
    felh=input("Felhasználónév: ")
    while felh not in adatok:
        hibak+=1
        #print(hibak)
        print("Nincs ilyen felhasználónév az adatbázisban!")
        felh=input("Felhasználónév: ")
        
        if hibak==3:
            print("-"*30)
            print("A hibák száma elérte a 3-at.Viszlát!")
            sys.exit()
    jel=input("Jelszó: ")
    while jel not in adatok:
        hibak+=1
        #print(hibak)
        print("Hibás jelszó!")
        jel=input("Jelszó: ")
        
        if hibak==3:
            print("-"*30)
            print("A hibák száma elérte a 3-at.Viszlát!")
            sys.exit()
    if felh and jel in adatok:
        print()
        print("Sikeres bejelenkezés!")
        print("-"*30)
        print("1.DDOS Tool")
        print("2.IP Tracker")
        user_valasztas=input("Az alábbiak közül válassz: ")
        if user_valasztas=="1":
            ddos()
        if user_valasztas=="2":
            def getDetails(ipAddress):
                r = get('http://ip-api.com/json/{0}'.format(ipAddress))
                data = loads(r.content)
                return data

            ipAddress = input("Add meg a trackelni kivánt IP-t: ")
            data = getDetails(ipAddress)
            for key, value in data.items():
                print(key, ":", value)

            
else:
    regfelh=input("Adj meg egy felhasználó nevet: ")
    regjel=input("Adj meg egy jelszót: ")
    print("Most inditsd újra a programot az adatbázis frissitése miatt!")
    f=open("adatbazis.txt","a")
    f.write("\n")
    f.write(regfelh)
    f.write("\n")
    f.write(regjel)
    f.write("\n")
    f.close()

