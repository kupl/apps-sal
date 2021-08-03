t = int(input())
for i in range(0, t):
    s = input()
    l = len(s)
    ans = 0
    for j in range(0, l):
        if s[j] == 'a' or s[j] == 'e' or s[j] == 'i' or s[j] == 'o' or s[j] == 'u':
            c = 1
        else:
            c = 0
        ans = ans + c * pow(2, l - 1)
        l = l - 1
    print(ans % 1000000007)
