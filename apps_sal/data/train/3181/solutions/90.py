def check_alive(health):
    if health <= 0 or health is None:
        return False
    elif health > 0:
        return True
