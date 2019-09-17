from random import randint

class Cup:
    
    def __init__(self, smaak):
        smaken = ["Java", "Espresso", "Cappucino", "Zwart", "Verkeerd", "Moccha", "Wiener Melange"]
        self.smaak = smaken[smaak]

    
class KoffieAutomaat:
    def __init__(self, merk, eersteVulling):
        cups = []
        self.cups = cups
        self.merk = merk
        self.vul(eersteVulling)

    def vul(self, aantal):

        for i in range(0,aantal):
            randomSmaak = randint(0,6)
            nieuwKopje = Cup(randomSmaak)
            self.cups.append(nieuwKopje)
            i += 1
    

    def koffieIsOp(self):
        if not self.cups:
            return True
        else:
            return False
    
    def zetKoffie(self):
        return self.cups.pop(0).smaak

    def lijstKopjes(self):
        kopLijst = ""

        for i in range(0, len(self.cups)):
            kopLijst += self.cups[i].smaak + ", "
            i += 1
        
        return self.merk + " automaat is gevuld met: " + kopLijst
    

dezeAutomaat = KoffieAutomaat("Philips", 3)
print(dezeAutomaat.lijstKopjes())

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
            stoppen = input("wil je stoppen?")
            if stoppen == "y":
                break
        
    print(dezeAutomaat.lijstKopjes())