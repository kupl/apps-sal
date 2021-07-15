def check_alive(health):
    Heal = True
    if health <= 0:
        Heal = False
    return Heal
