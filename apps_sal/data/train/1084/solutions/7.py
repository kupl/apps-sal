t = 1
for n in range(t):
    s = input()
    count = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            count += 1
    if s[len(s) - 1] == '0':
        count -= 1
    print(count)
