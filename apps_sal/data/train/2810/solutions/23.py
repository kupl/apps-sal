def solve(arr):
    counts = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(arr)):
        count = 0
        for j in range(min(len(arr[i]), len(alpha))):
            if arr[i][j].lower() == alpha[j]:
                count += 1
        counts.append(count)
    return counts
