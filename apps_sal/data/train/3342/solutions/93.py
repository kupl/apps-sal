def pattern(n):
    listNums = []
    listNums = [str(num) * num for num in range(1, n + 1)]
    return '\n'.join(listNums)
