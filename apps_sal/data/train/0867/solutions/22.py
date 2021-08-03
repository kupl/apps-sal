# n,k = map(int,input().strip().split(" ")) takes two number as input in a     single line
# arr = list(map(int,input().split())) takes an array as a input in a single     line
# arr = [int(input()) for i in range(n)] takes an array as input in different     lines


def solve():
    s, w1, w2, w3 = list(map(int, input().split()))
    k = w1 + w2 + w3
    if k <= s:
        ans = 1
    elif (k - w3 <= s) or (k - w1 <= s):
        ans = 2
    else:
        ans = 3
    print(ans)


t = int(input())
while t > 0:
    solve()
    t -= 1
