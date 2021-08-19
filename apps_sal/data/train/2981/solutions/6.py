def solution(n, d):
    if d >= len(str(n)):
        list_return = list(str(n))
        for i in range(len(list_return)):
            list_return[i] = int(list_return[i])
        return list_return
    if d <= 0:
        return []
    list_return = list(str(n)[-d:])
    for i in range(len(list_return)):
        list_return[i] = int(list_return[i])
    return list_return
