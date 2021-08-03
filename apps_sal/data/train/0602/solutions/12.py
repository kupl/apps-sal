s = list(input().split())
min = 999999999
r = ""
for i in range(len(s)):
    if(len(s[i]) < min):
        min = len(s[i])
        r = s[i]
print(r, end=' ')
for i in s:
    print(i + " " + r, end=' ')
# print(r,min)
