def extra_perfect(n):
    return [i for i in range(n+1) if all(map(int, [bin(i)[2], bin(i)[-1]]))]
