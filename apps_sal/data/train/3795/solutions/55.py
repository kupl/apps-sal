def combat(health, damage):
    return bool(health>damage)*(health-damage)
