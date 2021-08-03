def elevator(left, right, call):
    if int(right) == int(call) and int(left) == int(call):
        return("right")
    elif int(right) == int(call):
        return("right")
    elif int(left) == int(call):
        return("left")
    elif int(call) == 0 and int(left) < int(right):
        return("left")
    elif int(call) == 1 and int(left) > int(right):
        return("right")
    elif int(call) == 2 and int(left) > int(right):
        return("left")
    else:
        return("right")
