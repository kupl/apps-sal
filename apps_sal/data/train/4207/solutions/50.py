def sum_cubes(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum

    n = 6
    print((sum_cubes(n)))

    # your code here
