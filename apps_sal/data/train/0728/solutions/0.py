def diagonal_difference(matrix):
    l = sum(matrix[i][i] for i in range(N))
    r = sum(matrix[i][N - i - 1] for i in range(N))
    return abs(l - r)


matrix = []
N = eval(input())
for _ in range(N):
    matrix.append(list(map(int, input().split())))

print(diagonal_difference(matrix))
