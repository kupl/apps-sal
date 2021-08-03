import bisect
n, m = map(int, input().split())
lst = []
ans = []
a = int(input())
lst.append(a)
for i in range(1, n + m):
    x = int(input())
    if x == -1:
        y = lst.pop(-1)
        ans.append(y)
    else:
        index = bisect.bisect_right(lst, x)
        lst.insert(index, x)
for i in ans:
    print(i)
