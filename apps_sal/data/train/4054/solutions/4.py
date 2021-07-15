def score(x):
    return (x['norm_kill'] * 100
          + x['assist'] * 50
          + x['damage'] * 0.5
          + x['healing'] * 1
          + 2 ** x['streak']
          + x['env_kill'] * 500)

def scoring(array):
    return [x['name'] for x in sorted(array, key=score, reverse=True)]
