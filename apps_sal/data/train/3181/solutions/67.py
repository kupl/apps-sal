def check_alive(health):
    alive = True
    if health <= 0:
        alive = False
    return alive
