# cook your dish here
for _ in range(int(input())):
    s = input()
    m = 10**7 + 9
    i = 0
    j = len(s) - 1
    c = 1
    while i <= j:
        if s[i] == s[j] == '?':
            c = ((c % m) * (26 % m)) % m
            i += 1
            j -= 1
        elif s[i] == '?' or s[j] == '?' or s[i] == s[j]:
            i += 1
            j -= 1
        else:
            c = 0
            break
    print(c)
