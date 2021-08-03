def combat(health, damage):
    return [0, health - damage][damage < health]
