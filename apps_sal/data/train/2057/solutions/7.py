S = input()[::-1]
S1 = []

num = 0
for s in S:
    if s == 'b':
        num += 1
    else:
        S1.append(num)

S1 = S1[::-1]
r = 0
num = 1
for s in S1:
    r = (r + s * num) % 1000000007
    num = (num * 2) % 1000000007

print(r)
