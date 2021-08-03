def warn_the_sheep(queue):
    position = list(reversed(queue)).index("wolf")
    return f"Oi! Sheep number {position}! You are about to be eaten by a wolf!" if position != 0 else 'Pls go away and stop eating my sheep'
