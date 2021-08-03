for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    answer = (k * ((n // 2) + (n % 2)))
    print(answer)
