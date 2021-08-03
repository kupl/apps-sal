def combat(health, damage):
    return (damage < health) * (health - damage)
