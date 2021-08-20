for _ in range(int(input())):
    n = int(input())
    arr = [1, 9, 31]
    diff = [8, 22]
    if n == 1:
        print(arr[0])
    elif n == 2:
        print(arr[1])
    elif n == 3:
        print(arr[-1])
    else:
        has = 0
        for i in range(2, n - 1):
            value = diff[i - 1] - diff[i - 2]
            value = value + 6
            value = value + diff[-1]
            diff.append(value)
            value = value + arr[-1]
            arr.append(value)
        print(arr[-1] % (10 ** 9 + 7))
