def check_alive(health):
    if health <= 0:  # needs = because 0 health is also not alive!
        return False
    else:
        return True  # True and False need uppercase
