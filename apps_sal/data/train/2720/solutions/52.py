def solution(digits):
    lst = list(map(int, digits))
    answ = []
    for i in range(0, len(lst) - 4):
        x = lst[i:i + 5]
        z = ''
        for j in x:
            z += str(j)
        answ.append(int(z))
    return max(answ)
