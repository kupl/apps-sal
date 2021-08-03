# cook your dish here
n = int(input())
m = pow(10, 9) + 7
for i in range(n):
    s = list(input())
    c = [None] * len(s)
    for j in range(len(s)):
        c[j] = -1

    for j in range(len(s)):
        if(s[j] == 'a' or s[j] == 'i' or s[j] == 'e' or s[j] == 'o' or s[j] == 'u'):
            c[j] = 1
        else:
            c[j] = 0
    d = len(s) - 1
    a = 0
    for j in range(0, len(s)):
        k = pow(2, d)
        a += (k * c[j])
        d -= 1
    print(a)
