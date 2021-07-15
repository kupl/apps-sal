def elevator(left, right, call):
    difleft = left-call
    difright = right-call
    
    if(call == left and call != right):
        return "left"
    if(call == right):
        return "right"
    if(left == right):
        return "right"
    if(difleft == difright):
        return "right"
    if(left>right and call<right):
        return "right"
    if(right>left and call<left):
        return "left"
    if(call > right and call > left and right > left):
        return "right"
    if(call > left and left > right):
        return "left"
    else:
        return "right"
