def well(x):
    good_ideas = 0
    for idea in x:
        if idea == 'good':
            good_ideas += 1
    if 0 < good_ideas <= 2:
        return 'Publish!'
    elif 2 < good_ideas:
        return 'I smell a series!'
    else:
        return 'Fail!'
