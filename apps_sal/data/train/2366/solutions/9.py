def mi():
    return list(map(int, input().split()))


'\n5\n6\n3 9 4 6 7 5\n1\n1000000\n2\n2 1\n10\n31 41 59 26 53 58 97 93 23 84\n7\n3 2 1 2 3 4 5\n'
for _ in range(int(input())):
    n = int(input())
    a = list(mi())[::-1]
    m = a[0]
    ans = 0
    for i in range(n):
        if a[i] > m:
            ans += 1
        elif a[i] < m:
            m = a[i]
    print(ans)
