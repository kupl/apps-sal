def elevator(left, right, call):
    if abs(right - call) < abs(left - call): return 'right'
    elif abs(right - call) > abs(left - call): return 'left'
    elif abs(right - call) == abs(left - call): return 'right'


