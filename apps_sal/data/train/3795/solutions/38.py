def combat(health, damage):
    '''
    Create a combat function that takes the player's current health
    and the amount of damage recieved,
    and returns the player's new health.
    Health can't be less than 0.
    '''
    rest = health - damage
    if rest < 0:
        return 0
    return rest
