def divide(weight):
    flag = False
    for i in range(3,weight + 1):
        if i %2 == 0 and (weight - i) %2 == 0:
            flag = True
            break
    return flag

