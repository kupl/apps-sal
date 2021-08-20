def reverse(right):
    lastr = []
    while right:
        lastr.append(right[-1])
        right = [a - b for (a, b) in zip(right, right[1:])]
    return lastr[::-1]
