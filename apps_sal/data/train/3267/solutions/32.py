def well(x):
    good_ideas = x.count('good')
    if not good_ideas:
        return 'Fail!'
    elif good_ideas <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'
