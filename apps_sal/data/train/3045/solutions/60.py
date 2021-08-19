def elevator(left, right, call):
    close_left = abs(call - left)
    close_right = abs(call - right)
    if close_right <= close_left:
        return 'right'
    return 'left'
