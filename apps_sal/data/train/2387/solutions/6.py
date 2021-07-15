for _ in range(int(input())):
    s = int(input())
    k = s
    while s >= 10:
        num = s // 10
        s += s // 10
        s -= num * 10
        k += num
    print(k)
