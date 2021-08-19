# cook your dish here
for t in range(int(input())):
    a, b, c = [int(i) for i in input().split(" ")]
    r = c % a
    ans = c - r + b
    if ans > c:
        ans -= a
    print(ans)
