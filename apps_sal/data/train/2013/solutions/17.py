s = list(input())


f = False
for i in range(len(s)):

    if s[i] != "a":
        s[i] = chr(ord(s[i]) - 1)
        f = True
    else:
        if f:
            break
        elif i == len(s) - 1:
            s[i] = "z"

print("".join(s))
