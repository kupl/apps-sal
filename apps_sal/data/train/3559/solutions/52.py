def chromosome_check(sperm):
    template = "Congratulations! You're going to have "
    if 'Y' in sperm:
        return template + 'a son.'
    else:
        return template + 'a daughter.'
