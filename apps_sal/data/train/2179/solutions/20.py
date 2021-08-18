from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))


a, b, c = rint()

n = int(input())
x = list(rint())

ans = 0
for i in x:
    if i > b and i < c:
        ans += 1

print(ans)
