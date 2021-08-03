for i in range(int(input())):
    n1 = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    print(m * (n1 - 1))
