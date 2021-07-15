def friend(x):
    z=0
    friends = []
    while z < len(x):
        if len(x[z]) == 4: friends.append(x[z])
        z+=1
    return friends
