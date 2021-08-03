for _ in range(int(input())):
    n = int(input())
    array = [int(i) for i in input().split()]
    array.sort()

    stones1 = sum([array[i] for i in range(0, n, 2)])
    stones2 = sum([array[i] for i in range(1, n, 2)])
    print(max(stones2, stones1))
