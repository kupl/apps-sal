try:
    for t in range(int(input())):
        n = int(input())
        ans = n * n * n + (n - 1) ** 2
        if ans <= 10 ** 9 + 7:
            print(ans)
        else:
            print(ans) % (10 ** 9 + 7)
except:
    pass
