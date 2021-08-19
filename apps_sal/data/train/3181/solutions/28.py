def check_alive(health):
    val = True
    if health <= 10 and health >= -10:
        if health > 0:
            return True
        else:
            return False
    else:
        return 'Nombre non effectif'
