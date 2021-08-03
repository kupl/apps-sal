for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    l = ''
    for i in s:
        if i == ':':
            l += ':'
        l += i
    magnet = []
    iron = []
    n = len(l)
    ans = 0
    for i in range(n):
        if l[i] == 'I':
            while magnet != [] and abs(magnet[0] - i) > k:
                magnet.pop(0)
            if len(magnet) > 0:
                ans += 1
                magnet.pop(0)
            else:
                iron.append(i)
        elif l[i] == 'M':
            while iron != [] and abs(iron[0] - i) > k:
                iron.pop(0)
            if len(iron) > 0:
                ans += 1
                iron.pop(0)
            else:
                magnet.append(i)
        elif l[i] == 'X':
            while iron != []:
                iron.pop(0)
            while magnet != []:
                magnet.pop(0)
    print(ans)
