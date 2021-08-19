t = int(input())
for i in range(t):
    s = input()
    a = 'aeiou'
    cnt = 0
    for i in range(len(s)):
        x = s[i]
        arr = []
        for j in range(5):
            z = abs(ord(x) - ord(a[j]))
            arr.append(z)
        cnt += min(arr)
    print(cnt)
