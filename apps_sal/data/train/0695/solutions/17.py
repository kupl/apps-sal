test = int(input())
for i in range(0, test):
    (x, y, n) = map(int, input().split())
    counter = 0
    for i in range(0, n + 1):
        n = x ^ i
        m = y ^ i
        if m > n:
            counter = counter + 1
    print(counter)
