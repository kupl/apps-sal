for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        ans = []
        c = 1
        while c <= n:
            ans.append(c + 1)
            ans.append(c)
            c += 2
        print(*ans)
    else:
        aux = [n - 1, n, n - 2]
        ans = []
        c = 1
        while c <= (n - 3):
            ans.append(c + 1)
            ans.append(c)
            c += 2
        ans = ans + aux
        print(*ans)
