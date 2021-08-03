def warn_the_sheep(q): return 'Pls go away and stop eating my sheep' if q[-1] == 'wolf' else f'Oi! Sheep number {str(q[::-1].index("wolf"))}! You are about to be eaten by a wolf!'
