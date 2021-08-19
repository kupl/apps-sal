def solve(string, k):
    ind = 0
    (iron, mag) = ([], [])
    for i in string:
        if i == ':':
            ind += 1
        elif i == 'I':
            iron.append(ind)
        elif i == 'M':
            mag.append(ind)
        ind += 1
    (i, j) = (0, 0)
    li = len(iron)
    lm = len(mag)
    ans = 0
    while i < li and j < lm:
        if abs(iron[i] - mag[j]) <= k:
            ans += 1
            i += 1
            j += 1
        elif iron[i] > mag[j]:
            j += 1
        else:
            i += 1
    return ans


for _ in range(int(input())):
    ans = 0
    (n, k) = list(map(int, input().split()))
    s = input()
    real = [i for i in s.split('X') if len(i) > 0]
    ans += sum((solve(string, k) for string in real))
    print(ans)
