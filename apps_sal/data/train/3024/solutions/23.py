def friend(x):
    my_friends = []
    for i in range(len(x)):
        if(len(x[i]) == 4):
            my_friends.append(x[i])
    return my_friends
