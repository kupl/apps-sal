for _ in range(int(input())):
    n = int(input())
    l = list(map(str, input().split()))
    a = []
    for i in l:
        a.append(i)
    print(''.join(a))
