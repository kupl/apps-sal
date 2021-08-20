s = input()
k = 0
for x in range(0, len(s) - 2):
    for y in range(x + 1, len(s) - 1):
        for z in range(y + 1, len(s)):
            if s[x] == 'Q' and s[y] == 'A' and (s[z] == 'Q'):
                k += 1
print(k)
