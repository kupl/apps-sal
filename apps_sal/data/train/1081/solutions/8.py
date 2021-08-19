t = int(input())
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(t):
    s = input().lower()
    s = list(s.strip())
    new = []
    for j in s:
        j = lst.index(j)
        new.append(j)
    s.clear()
    for j in range(len(new)):
        if j == 0:
            s.append(new[0] + 98)
        elif j == 1:
            s.append(new[1] + 57)
        elif j == 2:
            s.append(new[2] + 31)
        elif j == 3:
            s.append(new[3] + 45)
        elif j == 4:
            s.append(new[4] + 46)
    new.clear()
    for j in s:
        new.append(j % 26)
    s = ''
    for j in new:
        s += lst[j]
    print(s.upper())
