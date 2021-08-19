def well(x):
    good_ideas = sum((1 for word in x if word == 'good'))
    if good_ideas > 2:
        return 'I smell a series!'
    elif good_ideas > 0:
        return 'Publish!'
    return 'Fail!'
