def well(x):
    goodIdeas = 0
    for k in x:
        if(k == "good"):
            goodIdeas += 1
    if goodIdeas > 2:
        return "I smell a series!"
    elif goodIdeas >= 1:
        return "Publish!"
    else:
        return 'Fail!'
