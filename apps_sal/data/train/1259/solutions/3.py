z = int(input())

for i in range(z):
    l, r = map(int, input().split())
    count = 0
    for i in range(l, r + 1):

        if i % 10 in [2, 3, 9]:
            count += 1

    print(count)
