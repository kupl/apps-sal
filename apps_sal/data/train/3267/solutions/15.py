def well(ideas):
    good = 0
    
    for idea in ideas:
        if idea == 'good':
            if good > 1:
                return 'I smell a series!'
            good += 1
    
    return 'Publish!' if good else 'Fail!'
