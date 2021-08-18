from functools import reduce


def num_to_arr(num):
    s = str(num)
    arr = [0] * 10
    for c in s:
        arr[int(c)] += 1
    return arr


def dist_digits(arr):
    dist = []
    for i in range(0, 10):
        if arr[i] > 0:
            dist.append(i)
    return dist


def all_combos(arr, m):
    combos = []
    if m == 1:
        for i in range(1, 10):
            if arr[i] > 0:
                combos.append([i])
        return combos

    if m > sum(arr):
        return []

    digits = dist_digits(arr)
    for d in digits:
        nextArr = [0] * 10
        for i in range(0, 10):
            if i == d:
                nextArr[i] = arr[i] - 1
            if i > d:
                nextArr[i] = arr[i]
        nextCombos = all_combos(nextArr, m - 1)
        for nextComb in nextCombos:
            nextComb.append(d)
        combos.extend(nextCombos)
    return combos


def complete_combos(arr):
    combos = []
    for i in range(1, len(arr)):
        combos.extend(all_combos(arr, i))
    return list([arr for arr in combos if sum(arr) % 3 == 0])


def fact(n, zeros=0):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return (n - zeros) * fact(n - 1)


def permus(combo):
    arr = [0] * 10
    for digit in combo:
        arr[digit] += 1
    duplicates = 1
    for i in range(0, 10):
        if arr[i] > 1:
            duplicates *= fact(arr[i])
    return fact(len(combo), zeros=arr[0]) // duplicates


def find_mult_3(num):
    comp_combos = complete_combos(num_to_arr(num))
    return [sum(map(permus, comp_combos)), reduce(lambda x, y: x * 10 + y, comp_combos[-1])]
