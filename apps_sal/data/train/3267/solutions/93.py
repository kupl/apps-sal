def well(x):
    count_good = x.count('good')
    if count_good ==1 or count_good ==2 :
        return 'Publish!'
    elif count_good > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'
