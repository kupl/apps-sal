import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == 1:
        print(1)
        print(*([1] * n))
    elif n % 2 == 0:
        print(2)
        print(*([1, 2] * (n // 2)))
    else:
        flag = 1
        v = 0
        ans = [1] * n
        for i in range(1, n):
            if flag and a[i - 1] == a[i]:
                flag = 0
            else:
                v ^= 1
            ans[i] = v + 1

        if flag and a[0] != a[-1]:
            ans[-1] = 3
            print(3)
            print(*ans)
        else:
            print(2)
            print(*ans)
