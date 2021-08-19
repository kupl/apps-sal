# cook your dish here
def solve():
    x, r, a, b = map(int, input().split())
    d = 2 * 3.14 * r
    td = x * d
    fm = d / abs(a - b)
    temp = fm * max(a, b)
    if td % temp == 0:
        return int(td // temp) - 1
    else:
        return int(td // temp)


t = int(input())
for loop in range(t):
    print(solve())
