POINTS = {'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}


def scoreboard(b):
    return sorted(({'name': p['name'], 'score': sum((v * p.get(k, 0) for (k, v) in POINTS.items()))} for p in b), key=lambda d: (-d['score'], d['name']))
