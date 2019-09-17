from random import randint

class Cup:
    
    def __init__(self, smaak):
        smaken = ["Java", "Espresso", "Cappucino", "Zwart", "Verkeerd", "Moccha", "Wiener Melange"]
        self.smaak = smaken[smaak]

    
class KoffieAutomaat:
    def __init__(self, merk, eersteVulling):
        self.cups = []
        self.merk = merk
        self.vul(eersteVulling)

    def vul(self, aantal):

        for i in range(0,aantal):
            randomSmaak = randint(0,6)
            nieuwKopje = Cup(randomSmaak)
            self.cups.append(nieuwKopje)
            i += 1
    

    def koffieIsOp(self):
        return not self.cups
    
    def zetKoffie(self, num):
        return self.cups.pop(num).smaak

    def lijstKopjes(self):
        kopLijst = ""

        for i in range(0, len(self.cups)):
            kopLijst += self.cups[i].smaak + ", "
            i += 1
        
        return self.merk + " automaat is gevuld met: " + kopLijst

    def smaakLocatie(self, gewensteSmaak):
        while True:
            for i in range (0,len(self.cups)):
                if self.cups[i].smaak == gewensteSmaak:
                    return i
                
            gewensteSmaak = input("Deze smaak hebben we momenteel niet. Kies een andere aub. \n")
    

dezeAutomaat = KoffieAutomaat("Philips", 3)
print(dezeAutomaat.lijstKopjes())

while True:
    if dezeAutomaat.koffieIsOp():
        erbij = int(input("Leeg! Hoeveel cups wil je erbij? \n"))
        dezeAutomaat.vul(erbij)
    else:
        antwoord = input("Wil je een kop koffie? (y/n) \n")
        if antwoord == "y":
            smaakAntwoord = input("Welke smaak wil je? \n")
            smaakAntwoordLocatie = dezeAutomaat.smaakLocatie(smaakAntwoord)
            print("1 kopje " + dezeAutomaat.zetKoffie(smaakAntwoordLocatie) + " wordt gezet.")
        else:
            print("Er wordt geen koffie gezet.")
            stoppen = input("wil je stoppen? (y/n) \n")
            if stoppen == "y":
                break
        
    print(dezeAutomaat.lijstKopjes())