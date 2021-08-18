t = int(input())
for i in range(t):
    current = 0
    count = 0
    n, k = [int(x) for x in input().split()]
    h = [int(y) for y in input().split()]
    for j in range(100000000):
        if current == h[-1]:
            break

        for aa in range(100000000):

            if abs(current - h[j]) <= k:
                current = h[j]
                break
            else:
                current += k
                count += 1
    print(count)
