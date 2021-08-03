
for _ in range(int(input())):
    N = int(input())
    p = bin(N)[2:]
    ans = 0
    cnt = 0
    p = p[-1::-1]
    for i in p:
        ans += (int(i) * 6 ** cnt)
        cnt += 1
    print(ans)
