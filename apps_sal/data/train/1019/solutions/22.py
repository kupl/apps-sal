s = int(input())
for i in range(s):
    n = int(input())
    h = list(map(int, input().split()))
    d = 0
    if n % 2 != 0:
        c = n // 2
        if h[0] == 1:
            for i in range(1, c + 1):
                if h[i] - h[i - 1] == 1:
                    d = d + 1
            for i in range(c, len(h) - 1):
                if h[i] - h[i + 1] == 1:
                    d = d + 1
            if d == n - 1:
                print('yes')
            else:
                print('no')
        else:
            print('no')
    else:
        print('no')
