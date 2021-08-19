for i in range(int(input())):
    (n, k) = map(int, input().split())
    li = input().split()
    li1 = li[:n - k]
    li2 = li[n - k:]
    dict = {'H': 'T', 'T': 'H'}
    hd = 'H'
    for i in li2[::-1]:
        if i == hd:
            hd = dict[hd]
    print(li1.count(hd))
