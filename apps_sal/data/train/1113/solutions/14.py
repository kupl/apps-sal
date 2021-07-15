from array import array
def solve():
    n = int(input())
    inp = list(map(int, input().split()))
    mx = max([inp.count(i) for i in inp])
    ans = min([x for x in inp if inp.count(x) == mx])
    print(str(ans) + " " + str(inp.count(ans)))

t = int(input())
for i in range(0, t): solve()
