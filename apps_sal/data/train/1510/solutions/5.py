# cook your dish here
t = int(input())
for i in range(t):
    s = input()
    ms = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    ct = 0
    i = 0
    while ms != []:
        if s[i] in ms:
            ind = ms.index(s[i])
            ms.pop(ind)
            ct += 1
        else:
            ct += 1
        i += 1
    print(ct)
