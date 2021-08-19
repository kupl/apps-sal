MOD = 10 ** 9 + 7
faltu = eval(input())
theList = list(map(int, input().split()))
tcase = eval(input())
for times in range(tcase):
    (left, right) = list(map(int, input().split()))
    sub = sorted(theList[left - 1:right])
    sol = 0
    for index in range(1, right - left + 1):
        sol += (sub[index] - sub[index - 1]) ** 2
    print(sol)
