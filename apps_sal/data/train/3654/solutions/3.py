def divisible_count(x, y, k):
    ans = 0

    while True:
        if x % k == 0:
            break
        else:
            x += 1

    while True:
        if y % k == 0:
            break
        else:
            y -= 1

    ans = ((y - x) // k) + 1

    return ans
