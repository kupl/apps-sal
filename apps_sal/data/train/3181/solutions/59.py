def check_alive(health):
    if (health == 0):
        return False
    else:
        if (health < 0):
            return False
        else:
            return True
