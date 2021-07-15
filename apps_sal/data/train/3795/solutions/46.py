def combat(health, damage):
    newhealth = health - damage
    return 0 if newhealth < 0 else newhealth
