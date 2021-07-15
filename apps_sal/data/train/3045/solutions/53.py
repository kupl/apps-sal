def elevator(left, right, call):
    if abs(right-call)==abs(left-call):
        return 'right'
    elif abs(right-call)<abs(left-call):
        return 'right'
    else:
        return 'left'
