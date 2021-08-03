def solution(x):
    a = ''
    i = 0
    while i <= len(x) - 5:
        a += x[i:i + 5] + ' '
        i += 1
    return int(max(a.split()))
