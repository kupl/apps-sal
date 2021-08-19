n = int(input())
for i in range(n):
    s = input().strip()
    c = 0
    I = 0
    J = len(s) - 1
    while I < J:
        c += abs(ord(s[I]) - ord(s[J]))
        I += 1
        J -= 1
    print(c)
