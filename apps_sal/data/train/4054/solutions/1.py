def scoring(array):
    return [i['name'] for i in sorted(array, key=lambda x: x['norm_kill'] * 100 + x['assist'] * 50 + x['damage'] * 0.5 + x['healing'] + 2 ** x['streak'] + x['env_kill'] * 500, reverse=True)]
