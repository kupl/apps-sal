t = 0
try:
    t = int(input())
except:
    pass
for _ in range(t):
    s = input()
    x = 0
    if s[0] == '0':
        print(x)
    else:
        last = 0
        for i in range(0, len(s)):
            if s[i] == '0':
                x += 1
                if i < len(s) - 1:
                    if s[i + 1] == '1':
                        break
            else:
                last = 1
        print(x)
