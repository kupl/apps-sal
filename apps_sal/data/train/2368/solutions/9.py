for _ in range(int(input())):
    n = int(input())
    candies = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    min_c = min(candies)
    min_o = min(oranges)
    moves = 0
    for i in range(n):
        a = candies[i]
        b = oranges[i]
        x = a - min_c
        y = b - min_o
        moves += min(x, y) + max(x, y) - min(x, y)
    print(moves)
