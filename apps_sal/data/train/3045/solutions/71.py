def elevator(left, right, call):
    rt = abs(call - right)
    lt = abs(call - left)
    return "left" if rt > lt else "right"
