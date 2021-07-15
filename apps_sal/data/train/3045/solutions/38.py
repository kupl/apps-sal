def elevator(left, right, call):
    l = ['left', 'right']
    return l[abs(left - call) >= abs(right - call)]
