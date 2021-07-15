def x(n):
    arr = [['□'] * n for _ in range(n)]
    for i in range(len(arr)):
        arr[i][i]=arr[i][-1-i]='■'
    return "\n".join(["".join(i) for i in arr])
