def solve(arr):
    temp = {}
    answer = []
    for single in set(arr):
        temp[single] = [i for (i, x) in enumerate(arr) if x == single][-1]
    for (k, v) in sorted(temp.items(), key=lambda x: x[1]):
        answer.append(k)
    return answer
