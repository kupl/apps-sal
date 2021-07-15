def warn_the_sheep(queue):   
    return ["Oi! Sheep number %s! You are about to be eaten by a wolf!" % queue[::-1].index('wolf'),
            "Pls go away and stop eating my sheep"]['wolf' in queue[-1]]
