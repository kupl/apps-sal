def scoring(array):
    score_table = {'norm_kill': 100, 'assist': 50, 'damage': 0.5, 'healing': 1, 'env_kill': 500}
    scores = [(-sum((p[stat] * v for (stat, v) in score_table.items())) - 2 ** p['streak'], i, p['name']) for (i, p) in enumerate(array)]
    return [name for (s, i, name) in sorted(scores)]
