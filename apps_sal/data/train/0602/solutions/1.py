s = input()
s = s.split(" ")

# print(s)
a = []
s1 = []
for _ in range(len(s)):
    if s[_] != '':
        s1.append(s[_])
for _ in range(len(s1)):
    a.append(len(s1[_]))
# print(a)
aa = a.index(min(a))
ss = s1[aa]
print(ss, end=" ")
for _ in range(len(s1)):
    print(s1[_], ss, end=" ")
    # print(ss,end=" ")
