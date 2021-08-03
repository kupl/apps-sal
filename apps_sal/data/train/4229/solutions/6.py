def bits_war(numbers):
    res = [0, 0]
    for x in filter(None, numbers):  # To remove the 0 for the division
        res[x & 1] += bin(x).count('1') * x // abs(x)
    return "odds win" if res[0] < res[1] else "evens win" if res[0] > res[1] else "tie"
