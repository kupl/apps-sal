def well(x):
    goodCount = 0
    for item in x:
        if item == "good":
            goodCount += 1
            
    if goodCount > 2:
        return "I smell a series!"
    elif goodCount > 0:
        return "Publish!"
    else:
        return "Fail!"
