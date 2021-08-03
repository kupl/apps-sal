def invite_more_women(arr):
    i = []
    n = []
    for number in arr:
        if number < 0:
            n.append(number)
        else:
            i.append(number)
    if len(i) > len(n):
        return True
    else:
        return False
