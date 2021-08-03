for t in range(int(input())):
    n, m = list(map(int, input().split()))
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    colli = 0
    for i in range(m):
        count = 0
        for j in range(n):
            if matrix[j][i] == '1':
                count += 1
        if count > 1:
            colli += ((count * (count - 1)) // 2)
    print(colli)
