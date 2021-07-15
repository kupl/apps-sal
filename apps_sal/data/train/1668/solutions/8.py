def next_smaller(n):
    num = list(str(n))

    try:
        pivot = next(i for i in reversed(range(len(num) - 1)) if num[i] > num[i + 1])
    except StopIteration:
        return -1
    swap  = next(i for i in reversed(range(len(num))) if num[pivot] > num[i])

    num[pivot], num[swap] = num[swap], num[pivot]
    num[pivot + 1:] = reversed(num[pivot + 1:])

    if num[0] == '0':
        return -1

    return int(''.join(num))
