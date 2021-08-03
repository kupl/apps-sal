# cook your dish here
for t in range(int(input())):
    a = input().strip()
    c = 0
    n = len(a)
    for i in range(n // 2):
        c += abs(ord(a[i]) - ord(a[n - i - 1]))
    print(c)
