t = int(input())
for _ in range(t):
    (n, k) = [int(d) for d in input().split()]
    l = [int(d) for d in input().split()]
    a1 = min(l)
    l1 = []
    for i in range(n):
        l1.append(k ** (l[i] - a1))
    left_sum = 0
    right_sum = 0
    left = 0
    right = n - 1
    if k == 1:
        print(n // 2)
    elif n <= 3:
        if n == 2:
            print(1)
        elif l1[left] > l1[right]:
            print(1)
        elif l1[right] > l1[left]:
            print(2)
        else:
            print(1)
