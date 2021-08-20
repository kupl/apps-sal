def scoreboard(who_ate_what):
    return sorted(({'name': p['name'], 'score': 5 * p.get('chickenwings', 0) + 3 * p.get('hamburgers', 0) + 2 * p.get('hotdogs', 0)} for p in who_ate_what), key=lambda dict: (-dict['score'], dict['name']))
