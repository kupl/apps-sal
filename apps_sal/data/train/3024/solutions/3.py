def friend(x):
    myFriends = []
    for person in x:
        if len(person) == 4:
            myFriends.append(person)
    return myFriends
