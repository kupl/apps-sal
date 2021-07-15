def elevator(left, right, call):
    return 'right' if right == call or right == left or abs(right-call)<=abs(left-call) else 'left'
