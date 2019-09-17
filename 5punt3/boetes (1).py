MIN_SPEED = 50
MAX_SPEED = 110

def hoogteBoete(speed):
    
    if speed < (MIN_SPEED + 5):
        return "OK"
    elif speed > MAX_SPEED:
        return "Rijbewijs ingenomen"
    else:
        speed -= MIN_SPEED
        boete = int(speed / 5)
        boete = boete * 10
        return boete
        