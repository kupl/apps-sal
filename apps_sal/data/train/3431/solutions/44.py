def warn_the_sheep(queue):
    wolf = len(queue) - queue.index('wolf') - 1

    if not wolf:
        return 'Pls go away and stop eating my sheep'

    return f'Oi! Sheep number {wolf}! You are about to be eaten by a wolf!'
