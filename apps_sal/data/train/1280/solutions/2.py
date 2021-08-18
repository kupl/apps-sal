t = int(input())
for _ in range(t):
    l = input().strip()
    s = 0
    for i in range(len(l) // 2):
        s = s + (abs(ord(l[i]) - ord(l[len(l) - i - 1])))
    print(s)
