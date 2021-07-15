def solution(n):
    fint = int(n)
    diff = n - fint
    if diff < 0.25:
        rdiff = 0
    if diff >= 0.25 and diff < 0.75:
        rdiff = 0.5
    if diff >= 0.75:
        rdiff = 1
    rounded = rdiff + fint
    return rounded

