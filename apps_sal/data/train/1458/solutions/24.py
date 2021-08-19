for _ in range(int(input())):
    n = int(input())
    count_odd_square = 0
    for i in range(1, n + 1, 2):
        k = n - i + 1
        count_odd_square += k * k
    print(count_odd_square)
