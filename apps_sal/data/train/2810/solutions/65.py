def solve(arr):
    return [sum(1 if ord(i.lower()[j])-96==j+1 else 0 for j in range(len(i))) for i in arr]
