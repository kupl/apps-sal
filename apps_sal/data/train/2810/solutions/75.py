def solve(arr):
    output = [0] * len(arr)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if ord(arr[i][j].lower()) - 97 == j:
                output[i] += 1
    return output
