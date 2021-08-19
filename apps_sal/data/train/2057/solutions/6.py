S = input()[::-1]
num = 0
r = 0
for s in S:
    if s == 'a':
        r = (r + num) % 1000000007
        num = num * 2 % 1000000007
    else:
        num = num + 1
print(r)
