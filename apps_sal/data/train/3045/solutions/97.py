def elevator(left, right, call):
    return 'right' if left == call and right == call else 'right' if right == call else 'left' if left == call else 'right' if left - call == right - call else 'left' if abs(left - call) < abs(right - call) else 'right' 
