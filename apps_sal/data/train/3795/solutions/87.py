def combat(health: int, damage: int) -> int:
    return health - damage if health > damage else 0
