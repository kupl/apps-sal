def check_alive(health):
    if(-10 <= health <= 0):
        return False
    elif 0 < health <= 10:
        return True
