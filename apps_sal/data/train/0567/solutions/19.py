t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    x = [0] * n
    for i in range(n - 2):
        x[i] = x[i + 1] = x[i + 2] = l[i]
    if x == l:
        print('Yes')
    else:
        if n == 3:
            print('No')
        elif n == 4:
            if (l[0] == l[1] and l[1] == l[2]) or (l[-1] == l[-2] and l[-2] == l[-3]):
                print('Yes')
            else:
                print('No')
        else:
            for j in range(n - 1, 1, -1):
                if l[j] != x[j]:
                    x[j] = x[j - 1] = x[j - 2] = l[j]

            if x == l:
                print('Yes')
            else:
                print('No')
