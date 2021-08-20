def count_sheep(n):
    nums = [x for x in list(range(1, n + 1))]
    sheep = []
    for i in nums:
        sheep.append(str(i) + ' sheep...')
    sheep = ''.join(sheep)
    return sheep
