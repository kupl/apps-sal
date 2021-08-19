# cook your dish here
for _ in range(int(input())):
    d = {}
    for __ in range(int(input())):
        name = str(input())
        time = int(input())
        d[time] = name
        d = dict(sorted(d.items()))
    for v in d.values():
        print(v)
