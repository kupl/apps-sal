t = int(input())
for i in range(0, t):
    s = input()
    l = []
    f = 0
    m = 0
    for j in s:
        if j == "<":
            l.append("<")
        elif j == ">" and len(l) > 0:
            l = l[:-1]
            f = f + 2
            if l == []:
                m = f
        else:
            break
    print(m)
