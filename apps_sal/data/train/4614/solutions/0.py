def scoreboard(who_ate_what):
    scores = {'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}
    return sorted((
        {'name': person.pop('name'),
         'score': sum(scores.get(k, 0) * v for k, v in list(person.items()))}
        for person in who_ate_what), key=lambda a: (-a['score'], a['name']))

