def paul(x):
    vals = {'kata':5,'Petes kata':10,'life':0,'eating':1}
    score = 0
    for item in x:
        score += vals[item]
    if score < 40:
        return "Super happy!"
    elif score < 70:
        return "Happy!"
    elif score < 100:
        return "Sad!"
    else:
        return "Miserable!"
