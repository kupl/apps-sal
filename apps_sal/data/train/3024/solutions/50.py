def friend(x):
    friends = []
    for i in range(0, len(x)):
        currentFriend = x[i]
        if len(currentFriend) == 4:
            friends.append(currentFriend)
    return friends
