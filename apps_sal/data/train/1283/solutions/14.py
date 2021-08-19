p = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
e = [2 * i for i in p]
od = []
for i in range(len(p)):
    for j in range(i + 1, len(p)):
        if p[i] * p[j] <= 200:
            od.append(p[i] * p[j])
        else:
            break
    if j == i + 1:
        break
od.sort()
for i in range(int(input())):
    ans = 0
    n = int(input())
    if n % 2 == 0:
        for i in range(len(od)):
            for j in range(i, len(od)):
                if od[i] + od[j] == n:
                    ans = 1
                    break
                if od[i] + od[j] > n:
                    break
            if ans == 1 or j == i:
                break
        if ans == 0:
            for i in range(len(e)):
                for j in range(i, len(e)):
                    if e[i] + e[j] == n:
                        ans = 1
                        break
                    if e[i] + e[j] > n:
                        break
                if ans == 1 or j == i:
                    break
    else:
        for i in range(len(e)):
            for j in range(len(od)):
                if e[i] + od[j] == n:
                    ans = 1
                    break
                if e[i] + od[j] > n:
                    break
            if ans == 1 or j == 0:
                break
    if ans == 1:
        print('YES')
    else:
        print('NO')
