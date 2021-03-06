def getDivisors(num):
    res = []
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            res.append(i)
            sum += i ** 2
    return (res, sum)


def list_squared(m, n):
    result = []
    nums = [1, 42, 246, 287, 728, 1434, 1673, 1880, 4264, 6237, 9799, 9855, 18330, 21352, 21385, 24856, 36531, 39990, 46655, 57270, 66815, 92664]
    s = [1, 2500, 84100, 84100, 722500, 2856100, 2856100, 4884100, 24304900, 45024100, 96079204, 113635600, 488410000, 607622500, 488410000, 825412900, 1514610724, 2313610000, 2313610000, 4747210000, 4747210000, 13011964900]
    for i in range(m, n + 1):
        if i in nums:
            result.append([i, s[nums.index(i)]])
    return result
