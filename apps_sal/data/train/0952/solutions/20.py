import math
alpha = "abcdefghijklmnopqrstuvwxyz"
vow = 'aeiou'
for t_itr in range(int(input())):
    s = str(input())
    count = 0
    for i in s:
        if i in vow:
            count += 0
        else:
            a = []
            a.append(abs(alpha.index(i) - alpha.index("a")))
            a.append(abs(alpha.index(i) - alpha.index("e")))
            a.append(abs(alpha.index(i) - alpha.index("i")))
            a.append(abs(alpha.index(i) - alpha.index("o")))
            a.append(abs(alpha.index(i) - alpha.index("u")))
            count += min(a)
    print(count)
