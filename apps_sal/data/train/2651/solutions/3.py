def prod2sum(a, b, c, d):
    num = [a, b, c, d]
    if sorted([abs(num[0] * num[2] - num[1] * num[3]), abs(num[0] * num[3] + num[1] * num[2])]) == sorted([num[0] * num[3] - num[1] * num[2], num[0] * num[2] + num[1] * num[3]]):
        return [sorted([abs(num[0] * num[3] + num[1] * num[2]), abs(num[0] * num[2] - num[1] * num[3])])]
    else:
        if sorted([abs(num[0] * num[3] - num[1] * num[2]), abs(num[0] * num[2] + num[1] * num[3])])[0] < sorted([abs(num[0] * num[2] - num[1] * num[3]), abs(num[0] * num[3] + num[1] * num[2])])[0]:
            return [sorted([abs(num[0] * num[3] - num[1] * num[2]), abs(num[0] * num[2] + num[1] * num[3])]), sorted([abs(num[0] * num[2] - num[1] * num[3]), abs(num[0] * num[3] + num[1] * num[2])])]
        else:
            return [sorted([abs(num[0] * num[2] - num[1] * num[3]), abs(num[0] * num[3] + num[1] * num[2])]), sorted([abs(num[0] * num[3] - num[1] * num[2]), abs(num[0] * num[2] + num[1] * num[3])])]



