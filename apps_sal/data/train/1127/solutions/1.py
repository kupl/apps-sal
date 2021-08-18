for _ in range(int(input())):
    s = input()
    l = s.split()
    l[-1] = l[-1].title()
    for i in range(len(l) - 1):
        l[i] = l[i][0].upper() + "."
    print(*l)
