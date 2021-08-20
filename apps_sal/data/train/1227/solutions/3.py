indices = [[0, 2, 4], [0, 3, 4], [0, 2, 5], [0, 3, 5], [1, 2, 4], [1, 3, 4], [1, 2, 5], [1, 3, 5]]
for _ in range(int(input())):
    color = list(map(str, input().split()))
    ans = 'NO'
    for i in range(8):
        if color[indices[i][0]] == color[indices[i][1]] == color[indices[i][2]]:
            ans = 'YES'
            break
    print(ans)
