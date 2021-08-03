def find(n):
    return sum(set(range(0, n + 1, 3)) | set(range(0, n + 1, 5)))
