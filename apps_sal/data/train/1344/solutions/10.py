for _ in range(int(input())):
    n = int(input())
    l = [int(n) for n in input().split()]
    a = min(l)
    l.remove(a)
    b = min(l)
    print(a + b)
