def elevator(left, right, call):
    print(left, right, call)
    return 'right' if abs(left - call) >= abs(right - call) else 'left'
