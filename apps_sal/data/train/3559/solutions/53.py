def chromosome_check(sperm):
    res = ['son', 'daughter'][sperm == 'XX']
    return f'Congratulations! You\'re going to have a {res}.'
