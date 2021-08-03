for _ in range(int(input())):
    n, s, s2 = int(input()), 1, 1
    arr = list(map(int, input().split()))
    s = s * max(arr)
    arr.remove(max(arr))
    s *= max(arr)
    s2 *= min(arr)
    arr.remove(min(arr))
    s2 *= min(arr)
    print(s, s2)
