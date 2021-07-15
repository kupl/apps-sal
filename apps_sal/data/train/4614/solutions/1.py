PTS = {'name': 0, 'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}

def scoreboard(who_ate_what):
    return sorted( ({'name': d['name'],
                     'score': sum( d.get(what,0)*coef or 0 for what,coef in PTS.items())}
                    for d in who_ate_what),
                  key=lambda d: (-d['score'],d['name']))
