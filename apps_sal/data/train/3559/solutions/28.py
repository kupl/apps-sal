def chromosome_check(sperm):
    text = 'Congratulations! You\'re going to have a '
    return text + ('son.', 'daughter.')[sperm == 'XX']
