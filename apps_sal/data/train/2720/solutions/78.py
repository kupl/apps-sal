def solution(digits):
    n = []
    for i in range(0, len(digits)):
        s = str(digits)[i:i + 5]
        n.append(s)
    new = [int(i) for i in n]
    return max(new)
