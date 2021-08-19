t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    last_start = l[0]
    prev = l[0]
    for j in l[1:]:
        if j == prev + 1:
            prev = j
            continue
        prev = j
        if j >= last_start:
            print('No')
            break
        last_start = j
    else:
        print('Yes')
