def primo(n):
    ctr = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ctr = 1
            break
    if ctr:
        return False
    else:
        return True


t = int(input())
for i in range(t):
    (x, y) = list(map(int, input().split()))
    j = 1
    while primo(x + y + j) == False:
        j += 1
    print(j)
