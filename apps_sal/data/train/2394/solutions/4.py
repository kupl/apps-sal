for _ in range(int(input())):
    n = int(input())
    ar = list(input())
    kek = 0
    ans = 0
    for i in range(n):
        if ar[i] == '(':
            kek += 1
        else:
            kek -= 1
        if kek < 0:
            kek += 1
            ans += 1
    print(ans)
