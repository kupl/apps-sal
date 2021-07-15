def max_tri_sum(numbers):
    print(numbers)
    a = sorted([i for i in set(numbers)])
    return a[-1]+a[-2]+a[-3]
