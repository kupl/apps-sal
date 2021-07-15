def check_alive(health):
    if (health == 0):
        return False
    if(health < 10 and health > 0) or (health < 0 and health < -10):
        return True
    else:
        return False
