def find_digit(num, nth):
    nList = []
    num = str(num)
    for i in num:
        nList.append(i)
    
    if nth <= 0:
        return -1
    elif nth > len(nList):
        return 0
    
    for index,curr in enumerate(nList):
        if index == len(nList) - nth:
            return int(curr)

