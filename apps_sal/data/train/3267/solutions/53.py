def well(x):
    y = x.count("good")
    if y == 0:
        return "Fail!"
    elif y == 1 or y == 2:
        return "Publish!"
    else:
        return "I smell a series!"
