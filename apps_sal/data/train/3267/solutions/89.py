def well(x):
    res = 0
    for i in x:
        if i == 'good': res += 1
    if res <= 2 and res > 0: return 'Publish!'
    elif res > 2: return 'I smell a series!'
    else: return 'Fail!'
