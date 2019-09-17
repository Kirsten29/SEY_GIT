from random import randint #random is van Python zelf #randint (functie) importeer je uit module random van Python
​
class Cup:
    
    def __init__(self, smaakInput): #self in init, smaak in die regel hoeft niet. smaak i invoer wanneer je een nw cupobject aanmaakt
        smaken = ["Java", "Espresso", "Cappucino", "Zwart", "Verkeerd", "Moccha", "Wiener Melange"]
        self.smaak = smaken[smaakInput] 
​
    
class KoffieAutomaat: #lijst aanmaken met cups die in automaat zitten.
    def __init__(self, merk, eersteVulling):
        cups = []
        self.cups = cups
        self.merk = merk
        self.vul(eersteVulling) #wordt later gedefinieerd. Python kan dat, andere taal loopt hier vast.
​
    def vul(self, aantal):
​
        for i in range(0,aantal): #voor elk element in  bereik 0-6 pakt'ie een random smaak. (for refereert aan forloop, anders stond er while)
            randomSmaak = randint(0,6) #0 telt ook mee, als 1 dus,  dus (0,6) is 7 in totaal
            nieuwKopje = Cup(randomSmaak) #gebruikt eerder aangemaakte cuplijst
            self.cups.append(nieuwKopje)
            i += 1
    
​
    def koffieIsOp(self): #aangemaakt voor een andere functie
        if not self.cups:
            return True
        else:
            return False
    
    def zetKoffie(self):
        return self.cups.pop(0).smaak #element 0 uit cup lijst laten "poppen". zonder poppen zou'ie steeds 0 (Java) pakken. Poppen opzoeken! Haalt weg en ordent opnieuw .smaak is om smaak later in test te kunnen gebruiken
​
    def lijstKopjes(self): #geeft later aan hoeveel kopjes in de machine zitten.(totaal gedefinieerd, niet wb smaken)
        kopLijst = ""
​
        for i in range(0, len(self.cups)): #len= length definieren om niet oneindig te loopen.
            kopLijst += self.cups[i].smaak + ", " #smaak van elke cup opslaan in koplijst. 
            i += 1
        
        return self.merk + " automaat is gevuld met: " + kopLijst #merk vd machine (regel 14 en 45)
    
​
dezeAutomaat = KoffieAutomaat("Philips", 3) #automaat aanmaken die Philips genoemd is en die 3 cupjes. nw object van type koffieautomaat aangemaakt.
print(dezeAutomaat.lijstKopjes()) #lijstkopjes = functie binnen lijst koffieautomaat  en welk ekopjes erin zitten. line 35
​
while True:
    if dezeAutomaat.koffieIsOp(): 
        erbij = int(input("Leeg! Hoeveel cups wil je erbij?"))
        dezeAutomaat.vul(erbij)
    else:
        antwoord = input("Wil je een kop koffie? (y/n)")
        if antwoord == "y":
            print("1 kopje " + dezeAutomaat.zetKoffie() + " wordt gezet.")
        else:
            print("Er wordt geen koffie gezet.")
            stoppen = input("wil je stoppen?") #keuze ja of nee nog toevoegen zou netter zijn. extra stukje code. Graphical user interface schrijven; wordt complex. of loop ja of nee
            if stoppen == "y":
                break #stopt while, else etc.
        
    print(dezeAutomaat.lijstKopjes()) #lijst kopjes verandert als iemand koffie heeft gezet dus daarom opnieuw printen.wals laatste break van toepassing is wordt line 62 (print) niet gelezen.