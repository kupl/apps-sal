# cook your dish here
n = int(input())
for i in range(n):
    k = int(input())
    s = input()
    c = 0
    for i in range(0, k - 1):
        if (s[i] == s[i + 1]):
            c = c + 1
    print(c)
