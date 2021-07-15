for _ in range(int(input())):
    lenn, lenm = [int(x) for x in input().split()]
    n = [int(x) for x in input().split()]
    m = [int(x) for x in input().split()]
    answer = set(n) ^ set(m)
    print(*list(answer))
