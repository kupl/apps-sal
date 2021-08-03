def count_smaller(value, banlist):
    total = value
    for v in banlist:
        if v < value:
            total -= 1
    return total


cases = int(input())
for case in range(cases):
    n, m = map(int, input().split())
    banned = []
    for i in range(n):
        banned.append(int(input(), 2))
    desindex = ((1 << m) - n - 1) // 2
    candid = desindex
    while (count_smaller(candid, banned) < desindex) or (candid in banned):
        candid += 1
    print(bin(candid)[2:].zfill(m))
