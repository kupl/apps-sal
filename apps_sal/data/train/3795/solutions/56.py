def combat(health, damage):
    total = health - damage
    return total if total>0 else 0 
