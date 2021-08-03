# cook your dish here
# cook your dish here
l = int(input())
s = input()
i = 0
c = 0
s = list(s)
while i < len(s) - 1:
    if s[i] == s[i + 1]:
        c += 1
        s.remove(s[i])
        i -= 1
    i += 1
print(c)
