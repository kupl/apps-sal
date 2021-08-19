# cook your dish here
def generateIndex(indexes):
    ans = indexes[:]
    for i in range(1, 4):
        for j in indexes:
            temp = []
            for k in j:
                temp.append((k + i) % 4)
            ans.append(temp)
    return ans


def countScore(x, index):
    profit = []
    for i in range(4):
        profit.append(x[i][index[i]])
    profit.sort()
    ans = 0
    m = [25, 50, 75, 100]
    for i in range(4):
        temp = (m[i] * profit[i])
        if temp == 0:
            ans -= 100
        else:
            ans += temp
    return ans


def ind(t):
    if t == 3:
        return 0
    if t == 6:
        return 1
    if t == 9:
        return 2
    if t == 12:
        return 3


t = int(input())
total = 0
while t > 0:
    indexes = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1]]
    allIndex = generateIndex(indexes)
    t -= 1
    n = int(input())
    a = [0, 0, 0, 0]
    b = a[:]
    c = a[:]
    d = a[:]
    for _ in range(n):
        m, t1 = input().split()
        t1 = int(t1)
        if m == 'A':
            a[ind(t1)] += 1
        elif m == 'B':
            b[ind(t1)] += 1
        elif m == 'C':
            c[ind(t1)] += 1
        else:
            d[ind(t1)] += 1
    x = [a, b, c, d]
    ans = []
    for i in allIndex:
        ans.append(countScore(x, i))
    profit = max(ans)
    total += profit
    print(profit)
print(total)
