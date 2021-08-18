def moves(n1, n2, m):
    lower = min(n1, n2)
    sum = max(n1, n2) - lower
    coverage = (m * (m + 1)) / 2
    if(coverage < lower):
        sum = sum + (lower - coverage) * 2
    return sum


T = int(input())
while T > 0:
    T = T - 1
    list_num = [int(x) for x in input().split()]
    print(moves(list_num[0], list_num[1], list_num[2]))
