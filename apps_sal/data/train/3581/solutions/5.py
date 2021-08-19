def sea_sick(s):
    return ['No Problem', 'Throw Up'][s.count('~_') + s.count('_~') > 0.2 * len(s)]
