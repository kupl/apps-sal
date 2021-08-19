# Determine if the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

# XX = Female
# XY = Male
def chromosome_check(sperm):
    if sperm == 'XY':
        return 'Congratulations! You\'re going to have a son.'
    else:
        return 'Congratulations! You\'re going to have a daughter.'
