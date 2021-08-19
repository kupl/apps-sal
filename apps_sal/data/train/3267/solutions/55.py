def well(x):
    # your code here
    c = 0
    for i in x:
        if(i == "good"):
            c += 1
    if(0 < c <= 2):
        return "Publish!"
    elif(c > 2):
        return "I smell a series!"
    else:
        return "Fail!"
