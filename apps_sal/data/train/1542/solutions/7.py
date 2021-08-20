maxpoints = []


def maxvaluez(num, arr, sc):
    i = 0
    points = 0
    mult = 1
    while i < 8:
        if arr[i] == '.':
            points += sc[i]
            i += 1
        elif arr[i] == 'd':
            points += 2 * sc[i]
            i += 1
        elif arr[i] == 't':
            points += 3 * sc[i]
            i += 1
        elif arr[i] == 'D':
            mult = mult * 2
            points += sc[i]
            i += 1
        elif arr[i] == 'T':
            mult = mult * 3
            points += sc[i]
            i += 1
        else:
            i += 1
    points = points * mult
    maxpoints.append(points)
    return points


def maxpicker(num, arr, sc):
    for i in range(num - 7):
        maxvaluez(num, arr[i:], sc)
    return max(maxpoints)


try:
    t = int(input())
    for i in range(t):
        num = int(input())
        arr = input()
        sc = list(map(int, input().split()))
        print(maxpicker(num, arr, sc))
        maxpoints = []
except:
    pass
