import sys
l1 = []
l2 = []


def iss():
    for i in range(len(l1) - 1):
        if l1[i + 1] < l1[i]:
            return False
    for i in range(len(l2) - 1):
        if l2[i + 1] < l2[i]:
            return False
    return True


for q in range(int(input())):
    n = int(sys.stdin.readline())
    data = [int(i) for i in sys.stdin.readline().strip()]
    done = False
    for d in range(10):
        mnl2 = -1
        mxl1 = -1
        same = []
        l1 = []
        l2 = []
        ans = ['0'] * n
        for i in range(n):
            f = data[i]
            if f > d:
                l2.append(f)
                ans[i] = '2'

                if mnl2 == -1:
                    mnl2 = i
            elif f < d:
                ans[i] = '1'
                l1.append(f)
                mxl1 = i
            else:
                same.append(i)
        if not iss():
            continue
        good = True
        for s in same:
            if s > mxl1:
                ans[s] = '1'
            elif s < mnl2:
                ans[s] = '2'
            else:
                good = False
                break
        if not good:
            continue
        sys.stdout.write("".join(ans) + '\n')
        done = True
        break
    if not done:
        sys.stdout.write('-\n')
