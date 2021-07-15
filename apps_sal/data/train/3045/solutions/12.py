def elevator(left, right, call):
    return ['left', 'right'][abs(left - call) >= abs(right - call)]
