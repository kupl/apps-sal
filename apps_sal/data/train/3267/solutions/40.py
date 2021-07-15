def well(x):
    good_idea_num = x.count('good')
    if good_idea_num < 1:
        return 'Fail!'
    elif good_idea_num < 3:
        return 'Publish!'
    else:
        return 'I smell a series!'
