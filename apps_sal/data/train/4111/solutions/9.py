def sabb(s, value, happiness):
    return 'Sabbatical! Boom!' if sum(1 for x in s if x.lower() in 'sabbatical') + value + happiness > 22 else 'Back to your desk, boy.'
