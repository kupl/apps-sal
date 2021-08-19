def friend(x):
    friendList = []
    for (index, name) in enumerate(x):
        if len(name) == 4:
            friendList.append(name)
        else:
            pass
    return friendList
