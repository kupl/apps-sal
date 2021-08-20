def solve(a, b, c):
    k = c // a
    n = b
    while n <= c:
        n += a
    return n - a


ans = []
T = int(input())
for i in range(T):
    li = [int(x) for x in input().strip().split()]
    ans.append(solve(li[0], li[1], li[2]))
for ele in ans:
    print(ele)
