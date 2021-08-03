def invite_more_women(arr):
    # your code here
    x = 0
    y = 0
    for l in arr:
        if l == -1:
            x = x + 1
        elif l == 1:
            y = y + 1
    if x < y:
        return True
    else:
        return False
