3

s = list(input().strip())
for x in range(len(s)):
    if s[x] == '0':
        del s[x]
        break
    elif x == len(s) - 1:
        del s[x]

print("".join(s))
