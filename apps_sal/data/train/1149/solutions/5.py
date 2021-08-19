# cook your dish here
t = int(input())
for _ in range(t):
    s = input()
    s = [i for i in s]
    n = len(s)
    # print(n,'---')
    c = 1
    mc = 1
    for i in range(len(s)):
        if s[i] == '?' and s[abs(n - 1 - i)] == '?':
            s[abs(n - 1 - i)] = s[i] = 'a'

            c *= 26

        elif s[i] != s[abs(n - 1 - i)] and s[i] != '?' and s[abs(n - 1 - i)] != '?':
            c = 0
            mc = 0
            break
        c = c % 10000009

    print(c)
