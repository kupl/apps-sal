# cook your dish here
test = int(input())
for p in range(test):
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    l = []
    a = []
    maxim = 0
    l = list(map(int, input().split()))
    d = []
    for i in l:
        if i not in d:
            d.append(i)
    for i in range(0, len(l) - k + 1):
        x = l[i:i + k]
        # print(x)
        flag = 0
        for j in d:
            if j not in x:
                flag = 1
                break
        if sum(x) > maxim and flag == 0:
            maxim = sum(x)
            a = x[:]
    # print(a)
    print(maxim)
