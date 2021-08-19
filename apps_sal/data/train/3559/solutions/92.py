def chromosome_check(sperm):
    a = "Congratulations! You're going to have a "
    if 'Y' in sperm:
        b = 'son.'
    else:
        b = 'daughter.'
    return f'{a}{b}'
