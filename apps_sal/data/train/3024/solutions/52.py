def friend(x):
    resultList = []
    for friend in x:
        if len(friend) == 4:
            resultList.append(friend)
    return resultList
