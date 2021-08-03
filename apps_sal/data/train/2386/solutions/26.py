for _ in range(int(input())):
    n = int(input())
    s = set()
    for i in map(int, input().split()):
        if i not in s:
            print(i, end=' ')
        s.add(i)
    print()
