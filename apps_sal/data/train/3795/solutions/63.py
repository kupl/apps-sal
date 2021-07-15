def combat(health, damage):
    new_health = health - damage
    return max(new_health,0)
