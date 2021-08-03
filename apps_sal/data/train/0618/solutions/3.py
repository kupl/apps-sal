
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l1 = []
    for i in range(k):
        l1.append(l[-1 - i])
    l1.reverse()
    for i in l:
        l1.append(i)
    # print(l1)
    sums = sum(l1[:k])
    sumlist = [sums]
    for i in range(len(l1) - k):
        sumlist.append(sums - l1[i] + l1[i + k])
        sums = sums - l1[i] + l1[i + k]
    print(max(sumlist))
