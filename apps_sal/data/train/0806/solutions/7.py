T = int(input())
for t in range(T):
    n = int(input())
    y = list(map(int, input().split()))
    x = [n]
    i = 0
    prev = x[0]
    visited = [{}, {}, {}]
    element = 1
    cycle_length = -1
    cycle_start = -1
    while True:
        a = y[i]
        mod = prev % a
        div = mod / a
        digit = int(str(div)[2])
        if digit == 0:
            digit = int(str(prev // a)[0])
        if digit in visited[i]:
            cycle_length = element - visited[i][digit]
            cycle_start = visited[i][digit]
            break
        else:
            visited[i][digit] = element
        x.append(digit)
        prev = int(digit)
        element += 1
        i = (i + 1) % 3
    Q = int(input())
    for q in range(Q):
        idx = int(input())
        if idx < len(x):
            print(x[idx])
        else:
            idx -= cycle_start
            idx = idx % cycle_length
            print(x[cycle_start + idx])
