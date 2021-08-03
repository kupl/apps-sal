def chromosome_check(sperm):
    msg = 'Congratulations! You\'re going to have a '
    child = ('daughter.', 'son.')['Y' in sperm]
    return msg + child
