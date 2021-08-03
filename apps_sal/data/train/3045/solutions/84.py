def elevator(left, right, call):
    temp = [abs(call - left), abs(call - right)]
    if min(temp) == temp[0]:
        if min(temp) == temp[1]:
            return 'right'
        else:
            return 'left'
    else:
        return 'right'
