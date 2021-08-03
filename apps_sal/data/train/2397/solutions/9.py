import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    s = set()
    mid = 2**(m - 1) - 1

    flag = 0
    for i in range(n):
        x = int(sys.stdin.readline().strip(), 2)
        s.add(x)

        if x > mid and flag == 0:
            flag = 1
        elif x > mid and flag == 1:
            flag = 0
            mid -= 1
            while mid in s:
                mid -= 1

        elif x < mid and flag == 0:
            flag = 1
            mid += 1
            while mid in s:
                mid += 1
        elif x < mid and flag == 1:
            flag = 0

        else:
            if flag == 1:
                flag = 0
                mid -= 1
                while mid in s:
                    mid -= 1
            else:
                flag = 1
                mid += 1
                while mid in s:
                    mid += 1
    ans = bin(mid)[2:]
    ans = '0' * (m - len(ans)) + ans
    print(ans)
