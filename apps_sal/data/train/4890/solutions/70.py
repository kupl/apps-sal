def find_difference(a, b):
    x = 1
    y = 1
    for i in a:
        x = x * i
    for i in b:
        y = y * i
    return x-y if x-y>0 else y-x
