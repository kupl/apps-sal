def scoring(array):
    points = {'assist': lambda a: a * 50, 'damage': lambda a: a * 0.5,
              'streak': lambda a: 2**a, 'norm_kill': lambda a: a * 100,
              'healing': lambda a: a * 1, 'env_kill': lambda a: a * 500}

    sum_score = {e['name']: sum(points[k](v) for k, v in list(e.items()) if isinstance(v, int)) for e in array}

    return sorted(sum_score, key=sum_score.get, reverse=True)
