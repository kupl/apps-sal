def combat(health, damage):

    if (health - damage) < 0:
        new_health = 0
        return new_health

    else:
        new_health = health - damage
        return new_health
