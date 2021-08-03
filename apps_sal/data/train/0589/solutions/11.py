t = int(input())
for _ in range(t):
    path = str(input()).split('#')
    c = 0
    jump = 0
    for i in path:
        if len(i) > jump:
            jump = len(i)
            c += 1
    print(c)
