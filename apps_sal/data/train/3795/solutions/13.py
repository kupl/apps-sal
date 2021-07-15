def combat(health: int, damage: int) -> int:
    """ Get the player's new health bases on the received damage. """
    return health - damage if health - damage >= 0 else 0
