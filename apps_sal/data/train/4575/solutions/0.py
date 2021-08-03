def smallest_integer(matrix):
    nums = set(sum(matrix, []))
    n = 0
    while n in nums:
        n += 1
    return n
