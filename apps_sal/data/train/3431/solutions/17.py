def warn_the_sheep(queue):
    wolf_pos = queue[::-1].index("wolf")
    return ( 'Pls go away and stop eating my sheep' if wolf_pos == 0
             else 'Oi! Sheep number %s! You are about to be eaten by a wolf!' % wolf_pos )
