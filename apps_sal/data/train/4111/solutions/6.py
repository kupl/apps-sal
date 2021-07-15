def sabb(s, value, happiness):
    nb = len(list(c for c in s.lower() if c in 'sabticl'))
    return ['Back to your desk, boy.', 'Sabbatical! Boom!'][nb + value + happiness > 22]
