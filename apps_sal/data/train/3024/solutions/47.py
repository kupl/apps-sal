def friend(x):
    friends = []
    for i in x:
        count = len(i)
        if count == 4 and (not i.isnumeric()):
            friends.append(i)
        else:
            pass
    return friends
