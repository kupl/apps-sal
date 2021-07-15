def combat(health, damage):
    healthnew= health- damage
    if healthnew<0:
      healthnew= 0
    return healthnew
