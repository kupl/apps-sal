s = input().split(" ")
k = input()
l = "abcdefghijklmnopqrstuvwxyz"
a = 26 * [0]
n = len(k)
c = ""
for i in range(n):
    a[l.find(k[i])] += 1
for i in range(len(s)):
    x = s[i]
    m = len(x)
    if (m == n):
        b = 26 * [0]
        for j in range(m):
            b[l.find(x[j])] += 1
        if a == b and x != k:
            c += str(i + 1)
print("The antidote is found in " + c + ".")
