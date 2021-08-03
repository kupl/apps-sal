def elevator(left, right, call):
    sum1 = abs(call - left)
    sum2 = abs(call - right)
    if sum2 <= sum1:
        return "right"
    else:
        return "left"
