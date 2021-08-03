def solve(arr):
    return [sum(j.lower() == k for j, k in zip(i, "abcdefghijklmnopqrstuvwxyz")) for i in arr]
