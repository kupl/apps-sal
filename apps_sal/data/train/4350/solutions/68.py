def pre_fizz(n):
    myList = []
    num = 1
    while len(myList) < n:
        myList.append(num)
        num += 1
    return myList
