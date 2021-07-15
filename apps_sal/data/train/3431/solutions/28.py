def warn_the_sheep(queue):
    return (lambda x: f'Oi! Sheep number {x}! You are about to be eaten by a wolf!' if x \
                    else 'Pls go away and stop eating my sheep') (queue[::-1].index('wolf'))
