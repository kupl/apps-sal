q = int(input())
for i in range(q):
    x, y = list(map(int, input().split()))
    diff = y - x
    x = bin(x)[2:]
    y = bin(y)[2:]
    x = '0' * (len(y) - len(x)) + x
    newString = ''
    for j in range(len(x)):
        if x[len(x) - j - 1] == '0':
            if diff >= 2**j:
                newString += '1'
                diff -= 2**j
            else:
                newString += '0'
        else:
            newString += '1'
    newString = newString[::-1]
    tot = 0
    ns = len(newString)
    for i in range(ns):
        tot += int(newString[ns - i - 1]) * (2**i)
    print(tot)
