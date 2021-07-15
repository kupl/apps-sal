def well(x):
    a = sum(1 for i in x if i == "good")
    if a == 1 or a == 2:
        return "Publish!"
    elif a > 2:
        return "I smell a series!"
    else:
        return "Fail!"
