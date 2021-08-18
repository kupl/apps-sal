t = int(input())

for t in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    counter = 0
    current = a[0]
    for i in range(0, len(a)):
        if a[i] <= current:
            counter = counter + 1
            current = a[i]

    print(counter)
