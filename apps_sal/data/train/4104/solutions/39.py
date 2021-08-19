def max_tri_sum(numbers):
    num = list(set(numbers))
    num.sort(reverse=True)
    return sum(num[0:3])
