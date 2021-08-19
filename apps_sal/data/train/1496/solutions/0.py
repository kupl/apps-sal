# cook your dish here
MOD = 10**9 + 7
for _ in range(int(input())):
    s = input()
    ind = 1
    level = 1
    for i in range(len(s)):
        if s[i] == 'l':
            if level % 2 == 1:
                ind = ind * 2
            else:
                ind = ind * 2 - 1
        if s[i] == 'r':
            if level % 2 == 1:
                ind = ind * 2 + 2
            else:
                ind = ind * 2 + 1
        level += 1
        ind %= MOD
    print(ind)
