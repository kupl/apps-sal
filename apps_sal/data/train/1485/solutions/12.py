t = int(input())
for i in range(t):
    diff = []
    n = int(input())
    for j in range(n):
        c1 = 0
        c2 = 0
        l1 = list(map(int, input()))
        for k in range(n):
            if l1[k] == 1 and k < n // 2:
                c1 += 1
            elif l1[k] and k >= n // 2:
                c2 += 1
        diff.append(c1 - c2)
    current_diff = sum(diff)
    new = []
    for kk in range(len(diff)):
        new.append(abs(current_diff - 2 * diff[kk]))
    print(min(min(new), abs(current_diff)))
