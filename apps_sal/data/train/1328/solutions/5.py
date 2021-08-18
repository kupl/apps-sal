t = int(input())
for _ in range(t):
    n = input().strip()
    cnt = 0

    for i in n:
        if i != '4' and i != '7':
            cnt += 1

    print(cnt)
