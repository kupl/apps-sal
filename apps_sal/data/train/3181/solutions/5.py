def check_alive(health):
    if health in range(-10, 0):
        return False
    elif health == 0:
        return False
    else:
        return True
