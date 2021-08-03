t = int(input())

while t:
    n, k = input().split()
    n, k = int(n), int(k)
    a = [int(i) for i in input().split()]
    b = a[:k - 1]
    a = a + b

    max = sum(a[:k])
    temp = max
    for i in range(1, n):

        temp = temp - a[i - 1] + a[i + k - 1]

        if temp > max:
            max = temp

    print(max)

    t -= 1
