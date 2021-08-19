# cook your dish here
for _ in range(int(input())):
    d = {}
    n = int(input())
    for i in range(n):
        k, v = map(int, input().split())
        if(k <= 8):
            if(k not in d.keys()):
                d[k] = v
            else:
                if(d[k] < v):
                    d[k] = v
    print(sum(d.values()))
