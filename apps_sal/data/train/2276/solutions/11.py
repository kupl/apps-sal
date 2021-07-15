


def solve(matrix, col, N, M):
    if col == M:
        '''
        for row in matrix:
            print(row)
        print()
        '''

        ans = 0
        for row in matrix:
            if len(row) == 1:
                ans += row[0]
            else:
                ans += max(*row)

        return ans

    # girar la columna `col` N - 1 veces

    if N == 1:
        return solve(matrix, col + 1, N, M)

    ans = solve(matrix, col + 1, N, M)
    for _ in range(N-1):
        tmp = matrix[0][col]
        for n in range(1, N):
            matrix[n-1][col] = matrix[n][col]
        matrix[N-1][col] = tmp

        local_ans = solve(matrix, col + 1, N, M)
        if local_ans > ans:
            ans = local_ans

    return ans

def main():
    T = int(input())
    for t in range(T):
        N, M = list([int(x) for x in input().split()])

        matrix = []
        for n in range(N):
            matrix.append(
                list([int(x) for x in input().split()])
            )

        elements = []
        for n in range(N):
            for m in range(M):
                elements.append((matrix[n][m], m))

        elements.sort(reverse=True)

        candidates = []
        for t in elements:
            if t[1] not in candidates:
                candidates.append(t[1])
                if len(candidates) == N:
                    break

        simplified = []
        for n in range(N):
            row = []
            for m in candidates:
                row.append(matrix[n][m])
            simplified.append(row)

        ans = solve(simplified, 0, N, min(N, M))
        print(ans)

main()

