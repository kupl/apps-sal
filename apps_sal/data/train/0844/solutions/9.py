n, k = list(map(int, input().split()))
hit = [0] * n
count = 0
for i in range(k):
    cmd = input().split()
    if cmd[0] == 'CLICK':
        idx = int(cmd[1]) - 1
        if hit[idx] == 0:
            hit[idx] = 1
            count += 1
        else:
            hit[idx] = 0
            count -= 1
    else:
        hit = [0] * n
        count = 0
    print(count)
