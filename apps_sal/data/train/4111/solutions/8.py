def sabb(s, v, h):
    ss = sum(1 for i in s if i in 'sabbatical')
    return ("Back to your desk, boy.", "Sabbatical! Boom!")[sum([ss, v, h]) > 22]
