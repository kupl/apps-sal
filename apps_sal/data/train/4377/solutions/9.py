def solve(a, b):
    countA = 0
    countB = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            countA += 1
        elif a[i] < b[i]:
            countB += 1
    return f'{countA}, {countB}: that looks like a "draw"! Rock on!'if countA == countB else f'{countA}, {countB}: Alice made "Kurt" proud!' if countA > countB else f'{countA}, {countB}: Bob made "Jeff" proud!'
