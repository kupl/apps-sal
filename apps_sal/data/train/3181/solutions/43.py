def check_alive(health):
    if health < 0:
        return False
    if health == 0:
        return False
    else:
        return True
