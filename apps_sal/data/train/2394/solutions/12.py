t = int(input())
for case in range(t):
    n = int(input())
    s = input()
    low = 0
    ht = 0
    for i in range(n):
        if s[i] == ')':
            ht -= 1
        else:
            ht += 1
        low = min(low, ht)
    ans = -low
    print(ans)
