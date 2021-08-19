def chromosome_check(sperm):
    return "Congratulations! You're going to have a %s." % {'XX': 'daughter', 'XY': 'son', 'YX': 'son'}[sperm]
