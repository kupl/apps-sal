def combat(health: int, damage: int) -> int:
    return max(0, health - damage)
