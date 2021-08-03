case = int(input())
for i in range(case):
    n = int(input())
    ls = list(map(int, input().split()))
    ls.reverse()
    cnt = 0
    for j in range(n):
        if cnt >= ls[j]:
            pass
        else:
            cnt = ls[j]
        cnt += 1
    print(cnt - 1)
