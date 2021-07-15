def well(arr):
    good_ideas = str(arr).lower().count('good')
    return 'I smell a series!' if (good_ideas > 2) else 'Fail!' if not(good_ideas) else 'Publish!'
