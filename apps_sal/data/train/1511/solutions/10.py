def fema(s, k):
    iron = []
    mag = []
    sheet = 0
    ind = -1
    for i in s:
        ind += 1
        if i == ':':
            sheet += 1
        if i == 'I':
            iron.append(ind)
        if i == 'M':
            mag.append(ind)

    count = 0
    i, j = 0, 0
    while i < len(iron) and j < len(mag):
        if abs(iron[i] - mag[j]) <= k:
            count += 1
            i += 1
            j += 1
        else:
            if(iron[i] > mag[j]):
                j += 1
            else:
                i += 1
    return count


test = int(input())
while(test != 0):
    test -= 1
    n, k = list(map(int, input().split()))
    s = input()
    li = [st for st in s.split('X') if len(st) > 0]
    ans = sum(fema(st, k) for st in li)
    print(ans)
