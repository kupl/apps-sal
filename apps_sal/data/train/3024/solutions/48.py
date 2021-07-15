def friend(people):
    flag = False
    while flag != True:
        flag = True
        for x in people:
            if len(x) != 4:
                people.remove(x)
                flag = False
    return people
