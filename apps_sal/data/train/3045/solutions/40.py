def elevator(left, right, call):
    print(left, right, call)
    if call == right == left:
        return "right"
    elif call == left:
        return "left"
    elif call == right:
        return "right"
    elif abs(call - left) == abs(call - right):
        return "right"
    elif abs(call - left) < abs(call - right):
        return "left"
    else:
        return "right"
