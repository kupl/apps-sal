for tc in range(int(input())):
    N = int(input())
    ar = [[' '] * N for i in range(N)]
    a = b = 0
    for i in range(N):
        ar[a][b] = str(i + 1)
        a += 1
        b += 1
    a = 0
    b = N - 1
    for i in range(N):
        ar[a][b] = str(i + 1)
        a += 1
        b -= 1
    for row in ar:
        print(''.join(row))
