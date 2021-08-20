t = int(input())
for i in range(t):
    s = input()
    count = 0
    pre = 0
    ans = 0
    for val in range(len(s)):
        if s[val] == '#':
            if count > pre:
                ans += 1
                pre = count
            count = 0
        else:
            count += 1
    print(ans)
