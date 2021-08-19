def elevator(left, right, call):
    choice = 'right'
    if call != right:
        choice = ('left', 'right')[abs(call - left) >= abs(call - right)]
    return choice
