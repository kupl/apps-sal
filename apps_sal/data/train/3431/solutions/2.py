def warn_the_sheep(queue):
    return 'Pls go away and stop eating my sheep' if queue[-1] == 'wolf' else f"Oi! Sheep number {queue[::-1].index('wolf')}! You are about to be eaten by a wolf!"
