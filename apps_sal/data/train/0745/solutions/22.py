for t in range(int(input())):
    n = int(input())
    ht_array = [int(e) for e in input().split()]
    sum_of_array = sum(ht_array)
    ht_array[0] = 1
    for i in range(1, n):
        if ht_array[i] > ht_array[i - 1] + 1:
            ht_array[i] = ht_array[i - 1] + 1
    ht_array[n - 1] = 1
    for i in range(n - 2, -1, -1):
        if ht_array[i] > ht_array[i + 1] + 1:
            ht_array[i] = ht_array[i + 1] + 1
    max_height = max(ht_array)
    moves = sum_of_array - max_height * max_height
    print(moves)
