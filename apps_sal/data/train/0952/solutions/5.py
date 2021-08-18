st = 'Aabcdefghijklmnopqrstuvwxyz'
li = list(st)
l1 = ['b', 'c']
l2 = ['d', 'f', 'g']
l3 = ['h', 'j', 'k', 'l']
l4 = ['m', 'n', 'p', 'q', 'r']
l5 = ['s', 't', 'v', 'w', 'x', 'y', 'z']
t = int(input())
for _ in range(t):
    s = input()
    su = 0
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            su += 0
        else:
            if s[i] in l1:
                su = su + abs(1 - li.index(s[i]))
            if s[i] in l2:
                su = su + abs(5 - li.index(s[i]))
            if s[i] in l3:
                su = su + abs(9 - li.index(s[i]))
            if s[i] in l4:
                su = su + abs(15 - li.index(s[i]))
            if s[i] in l5:
                su = su + abs(21 - li.index(s[i]))
    print(su)
