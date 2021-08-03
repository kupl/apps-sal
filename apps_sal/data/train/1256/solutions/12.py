# cook your dish here
for _ in range(int(input())):

    n = int(input())
    l = list(map(int, input().split()))

    c2 = 0
    c = 0
    for i in l:

        if i == 2:
            c2 += 1
        if i > 2:
            c += 1

    print(c2 * c + (c * (c - 1)) // 2)
