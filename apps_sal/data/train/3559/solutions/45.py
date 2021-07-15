def chromosome_check(sperm):
    if 'Y' in sperm:
        return 'Congratulations! You\'re going to have a son.' 
    if not 'Y' in sperm: 
        return 'Congratulations! You\'re going to have a daughter.'
