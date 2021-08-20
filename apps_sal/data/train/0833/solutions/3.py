while True:
    try:
        (n, m) = list(map(int, input().strip().split()))
        matrix = []
        for row in range(n):
            matrix.append(list(map(int, input().strip().split())))
        queries = int(input())
        for q in range(queries):
            (y1, x1, y2, x2) = list(map(int, input().strip().split()))
            s = 0
            for y in range(y1 - 1, y2):
                s += sum(matrix[y][x1 - 1:x2])
            print(s)
    except:
        break
