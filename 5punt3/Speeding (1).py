
def speeding(x):
    if x <= 50:
        return "Pass"
    elif x <= 55:
        return "10 euros"
    elif x <= 60:
        return "20 euros"
    elif x <= 65:
        return "30 euros"
    elif x <= 70:
        return "40 euros"
    elif x <= 75:
        return "50 euros"
    elif x <= 80:
        return "60 euros"
    else:
        return "Goodbye License"
            

boete = speeding(40)
print(boete)