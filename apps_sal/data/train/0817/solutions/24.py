# cook your dish here
t = int(input())
w = []
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    a = s[0] ^ s[1]
    for i in range(n - 2):
        a = a ^ s[i + 2]
    w.append(a)
for i in w:
    print(i)
