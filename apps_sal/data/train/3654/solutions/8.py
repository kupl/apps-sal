def divisible_count(x, y, k):
    result = 0
    for i in range(x, y + 1):
        if i % k == 0:
            result += 1
            break
    result += (y - i) // k
    return result
