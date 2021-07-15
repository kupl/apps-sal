def warn_the_sheep(queue):
    return 'Pls go away and stop eating my sheep' if queue.pop() == 'wolf' else f"Oi! Sheep number {int(len(queue))-int(queue.index('wolf'))}! You are about to be eaten by a wolf!"
