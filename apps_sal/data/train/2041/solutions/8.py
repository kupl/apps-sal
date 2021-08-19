n = int(input())
t = list(map(int, input().split()))
t = [-1] + t

badIdx = []
nice = []


def getBadIdx():
    for i in range(1, n):
        if ((i % 2 == 0) and (t[i] <= t[i + 1])) or ((i % 2 == 1) and (t[i] >= t[i + 1])):
            badIdx.append((i, i + 1))


def checkBad(k):
    if ((k <= (n - 1)) and (((k % 2 == 0) and (t[k] <= t[k + 1])) or ((k % 2 == 1) and (t[k] >= t[k + 1])))) \
            or ((k - 1) >= 1 and (((k - 1) % 2 == 0) and (t[k - 1] <= t[k]) or ((k - 1) % 2 == 1) and (t[k - 1] >= t[k]))):
        return True
    for (i, j) in badIdx:
        if ((i % 2 == 0) and (t[i] <= t[j])) or ((i % 2 == 1) and (t[i] >= t[j])):
            return True

    return False


def swap(i, j):
    ith = t[i]
    t[i] = t[j]
    t[j] = ith


getBadIdx()

if len(badIdx) > 4:
    print(0)
else:
    (i, j) = badIdx[0]
    # for (i,j) in badIdx:
    for k in range(1, n + 1):
        if i != k and t[i] != t[k]:
            swap(i, k)
            if not(checkBad(k)):
                nice.append((i, k))
                swap(i, k)
            else:
                swap(i, k)

        if j != k and t[j] != t[k]:
            swap(j, k)
            if not(checkBad(k)):
                nice.append((j, k))
                swap(j, k)
            else:
                swap(j, k)

    print(len(set([tuple(sorted(t)) for t in nice])))
