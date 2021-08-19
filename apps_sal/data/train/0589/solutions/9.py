t = int(input())
for _ in range(t):
    w = str(input()).split('#')
    day = 0
    jump = 0
    for i in w:
        if len(i) > jump:
            jump = len(i)
            day += 1
    print(day)
