def chromosome_check(sperm):
    # Your code here
    if sperm[0:2] == "XY":
        return 'Congratulations! You\'re going to have a son.'
    if sperm[0:2] == "XX":
        return 'Congratulations! You\'re going to have a daughter.'
