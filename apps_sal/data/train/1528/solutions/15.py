for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(str, input().split()))
    while k:
        k -= 1
        if l[-1] == "H":
            for i in range(len(l)):
                if l[i] == 'H':
                    l[i] = 'T'
                else:
                    l[i] = 'H'
        l.pop()
    print(l.count("H"))
