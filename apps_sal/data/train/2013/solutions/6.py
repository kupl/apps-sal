def findNot(string, char):
    for i in range(len(string)):
        if string[i] != char:
            return i
    return len(string) - 1


s = input()
beg = findNot(s, "a")
res = s[0:beg]
for i in range(beg, len(s)):
    if i != beg and s[i] == "a":
        res += s[i:]
        break
    if s[i] == "a":
        res += "z"
    else:
        res += chr(ord(s[i]) - 1)
print(res)
