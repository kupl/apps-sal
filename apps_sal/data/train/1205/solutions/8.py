t = int(input())
while t > 0:
    s = input()
    length = len(s)
    ans = 0
    for l in range(length):
        for r in range(l, length):
            temp = s
            x = temp[:l]
            for i in range(l, r + 1):
                if temp[i] == '0':
                    x += '1'
                else:
                    x += '0'
            x += temp[r + 1:]
            for k in range(len(x) - 1):
                if x[k] == x[k + 1]:
                    ans += 1
    print(ans)

    t -= 1
