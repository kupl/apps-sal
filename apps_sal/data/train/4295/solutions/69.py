def balanced_num(number):
    num = str(number)
    if len(num) % 2 == 0:
        leftind = (len(num)/2)-1
        rightind = (len(num)/2)+1
    else:
        leftind = len(num)//2
        rightind = (len(num)/2)+1
    l = num[:int(leftind)]
    r = num[int(rightind):]
    if sum(int(x) for x in l) == sum(int(x) for x in r):
        return "Balanced"
    else:
        return "Not Balanced"
