def combat(health, damage):
    """ calculate remaining health """
    return (health > damage)*(health - damage)
