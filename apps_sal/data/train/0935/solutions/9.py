t = int(input())
for _ in range(t):
    n = int(input())
    steps = -1
    if n % 10 == 0:
        steps += 1
    elif n % 5 == 0:
        steps = 1
    else:
        steps = -1
    print(steps)
