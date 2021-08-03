def men_from_boys(x):
    return sorted(set([i for i in x if i % 2 == 0])) + sorted(set([i for i in x if i % 2 != 0]), reverse=True)
