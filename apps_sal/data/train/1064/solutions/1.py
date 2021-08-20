t = int(input())
for _ in range(t):
    s = input()
    if len(s) < 4:
        for i in range(len(s)):
            if s[i] == '?':
                s = s[:i] + 'A' + s[i + 1:]
    else:
        for i in range(len(s) - 1, -1, -1):
            x = s[i - 3:i + 1]
            xx = 'CHEF'
            for j in range(len(x)):
                if x[j] == '?':
                    x = x[:j] + xx[j] + x[j + 1:]
            if x == 'CHEF':
                s = s[:i - 3] + 'CHEF' + s[i + 1:]
        for i in range(len(s)):
            if s[i] == '?':
                s = s[:i] + 'A' + s[i + 1:]
    print(s)
