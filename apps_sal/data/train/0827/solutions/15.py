t = int(input())
for x in range(t):
    (n, k) = input().split()
    (n, k) = (int(n), int(k))
    str = input()
    i = 0
    count1 = 0
    total = 0
    i = 0
    while i < n:
        if str[i] == 'a':
            count1 = count1 + 1
        i = i + 1
    (count2, count3) = (0, 0)
    i = 0
    while i < n:
        if str[i] == 'a':
            count2 = count2 + 1
        elif str[i] == 'b':
            total = total + (k * count2 + k * (k - 1) * count1 // 2)
        i = i + 1
    print(total)
