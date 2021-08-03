def invite_more_women(arr):
    # your code here
    a, b = 0, 0
    for i in arr:
        if i == 1:
            a = a + 1
        if i == -1:
            b = b + 1

    if a == b or a < b:
        c = False
    else:
        c = True
    return c
