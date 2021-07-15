def warn_the_sheep(queue):
    queue.reverse()
    return f"Oi! Sheep number {queue.index('wolf')}! You are about to be eaten by a wolf!" if queue.index('wolf') > 0 else 'Pls go away and stop eating my sheep' 
