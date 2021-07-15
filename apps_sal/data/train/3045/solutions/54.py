def elevator(left, right, call):
    if left==right:
        return "right"
    else:
        return "left" if abs(left-call)<abs(right-call) else "right"
