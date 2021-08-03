SABBATICAL = set('sabbatical')


def sabb(s, value, happiness):
    if value + happiness + sum(c in SABBATICAL for c in s) > 22:
        return 'Sabbatical! Boom!'
    else:
        return 'Back to your desk, boy.'
