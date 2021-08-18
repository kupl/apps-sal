temp = []
t = int(input())
for _ in range(t):
    s = input()
    l = list(s)
    x = len(l) * 8

    i = 0
    y = 0
    while i < (len(l)):
        count = 0
        while i < (len(l) - 1) and l[i] == l[i + 1]:

            count += 1

            i += 1
        if count == 0:
            y += 8
        else:
            y += 40
        i = i + 1
    temp.append(x - y)
for i in temp:
    print(i)
