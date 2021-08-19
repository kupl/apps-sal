values = (('norm_kill', 100 .__mul__), ('assist', 50 .__mul__), ('damage', 0.5.__mul__), ('healing', 1 .__mul__), ('streak', 2 .__pow__), ('env_kill', 500 .__mul__))


def score(player):
    return sum((f(player[k]) for (k, f) in values))


def scoring(array):
    return [player['name'] for player in sorted(array, key=score, reverse=True)]
