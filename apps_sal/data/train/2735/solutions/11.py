def jumping_number(number):
    list = ([int(d) for d in str(number)])
    diffList = []

    for i in range(1, len(list)):
        diff = (list[i] - (list[i - 1]))
        if diff == 1 or diff == -1:
            diffList.append("Jumping!!")
        else:
            diffList.append("Not!!")

    if "Not!!" in diffList:
        return("Not!!")
    else:
        return("Jumping!!")
