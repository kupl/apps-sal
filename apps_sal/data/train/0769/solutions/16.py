t = int(input())
while t > 0:
    (m, n) = map(int, input().split())
    if m > n:
        for i in range(n, 0, -1):
            if m % i == 0 and n % i == 0:
                print(i)
                break
    else:
        for i in range(m, 0, -1):
            if m % i == 0 and n % i == 0:
                print(i)
                break
    t -= 1
