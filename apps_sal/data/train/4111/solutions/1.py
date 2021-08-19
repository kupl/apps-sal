def sabb(s, value, happiness):
    score = sum((c in 'sabticl' for c in s.lower())) + value + happiness
    return 'Sabbatical! Boom!' if score > 22 else 'Back to your desk, boy.'
