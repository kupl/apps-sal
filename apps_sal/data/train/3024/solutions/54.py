def friend(x):
    #Code
    friend_l=list()
    for name in x:
        if len(name) == 4:
            friend_l.append(name)
    return friend_l
