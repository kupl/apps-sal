S = input()

num = 1
r = 0
for s in S:
    if s == 'a':
        num = (num * 2) % 1000000007
    else:
        r = (r + num - 1) % 1000000007

print(r)
