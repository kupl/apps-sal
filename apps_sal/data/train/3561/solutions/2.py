def around_fib(n):
    numbers_fibonacci = [0, 1]
    for i in range(n - 1):
        numbers_fibonacci.append(numbers_fibonacci[i] + numbers_fibonacci[i + 1])
    chunks = []
    max1 = str(max(numbers_fibonacci))
    max3 = ''.join(sorted(max1))
    count = [max3.count(i) for i in max3]
    max1_count = [max(count), max3[count.index(max(count))]]
    k = 0
    while 25 * k < len(max1):
        chunks.append(max1[25 * k:25 * (k + 1)])
        k += 1
    return "Last chunk {}; Max is {} for digit {}".format(chunks[-1], max1_count[0], max1_count[1])
