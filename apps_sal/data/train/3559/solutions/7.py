def chromosome_check(sperm):
    d = 'Congratulations! You\'re going to have a daughter.'
    s = 'Congratulations! You\'re going to have a son.'
    return s if sperm.find("Y") == 1 else d
