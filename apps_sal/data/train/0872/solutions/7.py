for i in range(int(input())):
    n, a, b, k = list(map(int, input().split()))
    s = 0
    j = 2
    while s < k and j < n + 1:
        if j % a == 0 and j % b != 0:
            s += 1
        elif j % b == 0 and j % a != 0:
            s += 1
        j += 1
    if s == k:
        print("Win")
    else:
        print("Lose")
