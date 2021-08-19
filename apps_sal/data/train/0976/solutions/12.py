# cook your dish here
n = int(input())
a = list(map(int, input().split()))
#a = [1,1,3,4,1,2,2,2]
#n = 14
k = 0
l = 0
ans1 = 0
ans2 = 0
b = 0
c = 0
mark1 = 0
mark2 = 0
for i in range(0, n):
    if a[i] == 1 and mark1 == 0:
        b += 1
        k = i
        mark1 = 1
    elif a[i] == 1:
        b += 1
    elif a[i] == 2 and b == 1:
        b -= 1
        k = i - k + 1
        ans1 = max(ans1, k)
        mark1 = 0
    elif a[i] == 2:
        b -= 1
    elif a[i] == 3 and mark2 == 0:
        c += 1
        l = i
        mark2 = 1
    elif a[i] == 3:
        c += 1
    elif a[i] == 4 and c == 1:
        c -= 1
        l = i - l + 1
        ans2 = max(ans2, l)
        mark2 = 0
    elif a[i] == 4:
        c -= 1


def alt_solve(s):
    pre = []
    dep = []
    ma = 0

    for c in s:
        if c == 2 or c == 4:
            pre.pop()
            dep.pop()
            continue

        if not pre:
            pre.append(c)
            dep.append(1)

        elif c != pre[-1]:
            pre.append(c)
            dep.append(dep[-1] + 1)

        else:
            pre.append(c)
            dep.append(dep[-1])

        if dep:
            ma = max(ma, dep[-1])

    return ma


print(alt_solve(a), ans1, ans2)
