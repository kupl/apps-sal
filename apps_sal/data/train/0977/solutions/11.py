t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    for i in range(n - 1):
        if(i % 2 == 0):
            temp = s[i + 1]
            s[i + 1] = s[i]
            s[i] = temp
    for i in range(n):
        s[i] = chr(ord('z') - ord(s[i]) + ord('a'))
    s = "".join(s)
    print(s)
