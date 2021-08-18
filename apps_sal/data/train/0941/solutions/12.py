t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))

    count = 0

    for i in range(1, a + 1):
        for j in range(1, b + 1):

            if (i + j) % 2 == 0:
                count += 1

    print(count)
