def evil_code_medal(*t):
    return ('None', 'Bronze', 'Silver', 'Gold')[sorted(t, reverse=True).index(t[0])]
