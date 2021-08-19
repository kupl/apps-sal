def warn_the_sheep(q):
    return (f"Oi! Sheep number {q[::-1].index('wolf')}! You are about to be eaten by a wolf!", 'Pls go away and stop eating my sheep')['w' in q[-1]]
