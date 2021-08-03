def warn_the_sheep(q):
    return ["Oi! Sheep number %s! You are about to be eaten by a wolf!" % q[::-1].index('wolf'),
            "Pls go away and stop eating my sheep"]['wolf' in q[-1]]
