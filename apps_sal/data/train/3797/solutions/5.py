def find_the_ball(start, swaps):
    """ Where is the ball? """
    arr = [0] * 100000
    arr[start] = 1
    for (x, y) in swaps:
        arr[x], arr[y] = arr[y], arr[x]
    return arr.index(1)
