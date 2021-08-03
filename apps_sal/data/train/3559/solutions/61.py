def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format(('son', 'daughter')['X' == sperm[1]])
