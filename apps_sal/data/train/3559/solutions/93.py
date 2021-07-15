def chromosome_check(s):
    m = 'Congratulations! You\'re going to have a {}.'
    return m.format('son') if s[-1] == 'Y' else m.format('daughter')
