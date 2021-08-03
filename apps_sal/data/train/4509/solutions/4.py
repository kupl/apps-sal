def validate_rhythm(meter, score):
    scores = score.split('|')
    anacrusis = False
    if 16 % meter[1]:
        return 'Invalid rhythm'
    for i, score in enumerate(scores):
        sums = sum(16 / int(s) for s in score)
        if sums < meter[0] * 16 / meter[1]:
            if i == len(scores) - 1 or i == 0:
                anacrusis = True
            else:
                return 'Invalid rhythm'
        elif sums > meter[0] * 16 / meter[1]:
            return 'Invalid rhythm'
    if anacrusis:
        return 'Valid rhythm with anacrusis'
    else:
        return 'Valid rhythm'
