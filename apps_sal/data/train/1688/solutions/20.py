for _ in range(int(input())):
    n = int(input())
    sequence = list(map(int, input().split()[:n]))
    print(*sequence, sep='')
