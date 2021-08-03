def solution(string):

    a = list(string)

    for i in range(len(a) // 2):
        if len(a) == 0 or len(a) == 1:
            break
        else:
            tmp = a[i]
            a[i] = a[len(a) - 1 - i]
            a[len(a) - 1 - i] = tmp

    return ''.join(a)


pass
