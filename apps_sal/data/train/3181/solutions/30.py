def check_alive(health):
    if -11 < health < 1:
        return False
    elif 0 < health < 11:
        return True
