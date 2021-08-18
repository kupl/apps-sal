

def multiple_of_index(arr):
    b = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            b.append(arr[i])
    return b
