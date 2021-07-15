def elevator(left, right, call):
    if right == call: return 'right'
    elif left == call: return 'left'
    elif abs(left-call) < abs(right-call): return 'left'
    else: return 'right'
    

