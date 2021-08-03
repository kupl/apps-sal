for _ in range(int(input())):
    n = int(input())
    x = ""
    lst = []
    c = ['c', 'o', 'd', 'e', 'c', 'h', 'e', 'f']
    for __ in range(n):
        s = input()
        x = x + s
    for l in c:
        if l == 'c' or l == 'e':
            lst.append(x.count(l) // 2)
        else:
            lst.append(x.count(l))
    print(min(lst))
