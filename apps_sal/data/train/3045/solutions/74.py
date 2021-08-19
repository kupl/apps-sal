def elevator(left, right, call):
    # find absolute value of difference between L and call and R and call
    if abs(right - call) == abs(left - call):  # if equal, return right
        return 'right'
    else:  # return smallest number
        return ('right' if abs(right - call) < abs(left - call) else 'left')
