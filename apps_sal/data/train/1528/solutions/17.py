for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    f = input().split()
    leftovers = f[:n - k]
    removed = f[n - k:]
    seekin = 'H'
    flip = {'H': 'T', 'T': 'H'}
    for coin in removed[::-1]:
        if coin == seekin:
            seekin = flip[seekin]
    print(leftovers.count(seekin))
