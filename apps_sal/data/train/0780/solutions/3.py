for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    print(['EVEN', 'ODD'][n % m % 2])
