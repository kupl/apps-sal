s = input()
s = s.split(" ")

a = []
s1 = []
for _ in range(len(s)):
    if s[_] != '':
        s1.append(s[_])
for _ in range(len(s1)):
    a.append(len(s1[_]))
aa = a.index(min(a))
ss = s1[aa]
print(ss, end=" ")
for _ in range(len(s1)):
    print(s1[_], ss, end=" ")
