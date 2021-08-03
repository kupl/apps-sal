def elevator(left, right, call):
    lc = abs(call - left)
    rc = abs(call - right)
    return 'left' if lc < rc else 'right' if rc < lc else 'right'
