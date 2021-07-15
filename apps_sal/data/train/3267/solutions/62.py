def well(x):
    score = 0
    for count in range(len(x)):
        if x[count] == "good":
            score += 1
        else:
            continue
    if score > 0 and score < 3:
        return "Publish!"
    elif score > 2: 
        return "I smell a series!"
    else:
        return "Fail!"
    

