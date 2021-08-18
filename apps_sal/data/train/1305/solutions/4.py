t = int(input())
for i in range(t):
    b = int(input())
    g = []
    for i in range(b):
        s = []
        l = list(map(int, input().split()))
        for i in range(len(l)):
            if(l[i] == 1):
                s.append(i)
        if(len(s) == 1):
            g.append("SAFE")
        else:
            for i in range(len(s) - 1):
                if(s[i + 1] - s[i] >= 2):
                    g.append("SAFE")
                else:
                    g.append("UNSAFE")
    if "UNSAFE" in g:
        print("UNSAFE")
    else:
        print("SAFE")
