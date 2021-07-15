def divisible_count(x,y,k):
    mod = x % k
    if mod != 0:
        x += (k - mod)
    y -= y % k
    if x > y:
        return 0
    return (y - x) // k + 1
