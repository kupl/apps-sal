def bck():
    t = eval(input())
    for i in range(t):
        s = input()
        l = []
        ch = ''
        i = 0
        while i != len(s) - 1:
            ch = s[i] + s[i + 1]
            l.append(ch)
            i = i + 1
        l = set(l)
        print(len(l))


bck()
