for _ in range(int(input())):
    d = int(input())
    p2 = 10 ** 5
    p1 = p2 - 1
    p = p2 - 2
    div = d // p
    arr = []
    for i in range(div):
        arr.append(p1)
        arr.append(p2)
        arr.append(1)
    rem = d % p
    arr.append(rem + 1)
    arr.append(rem + 2)
    arr.append(1)
    print(len(arr))
    print(*arr)
