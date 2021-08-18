T = int(input())

for tc in range(T):
    n = int(input())
    count = 0
    while n:
        count += n // 100
        n = n % 100
        count += n // 50
        n = n % 50
        count += n // 10
        n = n % 10
        count += n // 5
        n = n % 5
        count += n // 2
        n = n % 2
        count += n // 1
        n = n % 1
    print(count)
