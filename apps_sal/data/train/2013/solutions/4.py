s = input()
table = "abcdefghijklmnopqrstuvwxyz"


def nextchar(x):
    index = table.index(x)
    return table[index - 1]
ans, start = "", 0
for i in range(len(s)):
    if s[i] != 'a':
        ans += nextchar(s[i])
        start = 1
        continue
    if s[i] == 'a' and start == 1:
        ans += s[i:len(s)]
        break
    ans += s[i]
if str(s).count('a') == len(s):
    ans = str(s)[0:len(s) - 1] + "z"
print(ans)
