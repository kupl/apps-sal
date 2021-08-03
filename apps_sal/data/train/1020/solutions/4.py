testCases = int(input())
for Case in range(testCases):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            if sum > 0:
                if l[i] > 0:
                    sum += l[i]
                else:
                    sum -= l[i]
            else:
                if l[i] > 0:
                    sum -= l[i]
                else:
                    sum += l[i]
        else:
            if sum > 0:
                if l[i] > 0:
                    sum -= l[i]
                else:
                    sum += l[i]
            else:
                if l[i] > 0:
                    sum += l[i]
                else:
                    sum -= l[i]
    # print('sum',sum)
    if sum < 0:
        s = (-1) * sum
    else:
        s = sum
    if k <= s:
        print(1)
    else:
        print(2)
