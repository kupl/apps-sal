def fill_val(i, j, n, mat):
    nonlocal val
    while j >= 0 and i < n:
        mat[i][j] = val
        val += 1
        i += 1
        j -= 1


for _ in range(int(input())):
    n = int(input())
    arr = [[0 for c in range(n)] for r in range(n)]
    val = 1

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                fill_val(i, j, n, arr)

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")

        print()
