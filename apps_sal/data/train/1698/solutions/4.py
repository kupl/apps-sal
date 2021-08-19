def dbl_linear(n):
    arr = [1]
    xi = yi = 0
    for i in range(n):
        (x, y) = (arr[xi] * 2 + 1, arr[yi] * 3 + 1)
        arr.append(min(x, y))
        if min(x, y) == x:
            xi += 1
        if min(x, y) == y:
            yi += 1
    return arr[n]
