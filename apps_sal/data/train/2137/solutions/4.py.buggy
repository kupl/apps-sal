import sys

line = sys.stdin.readline()
n, k = [int(i) for i in line.split()]
line = sys.stdin.readline()
_min = int(1e7)
_max = 0
accum = [0] * int(1e6 + 2)
for i in line.split():
    j = int(i)
    accum[j] += 1
    if j > _max:
        _max = j
    if j < _min:
        _min = j

for i in range(1, _max + 1):
    accum[i] += accum[i - 1]
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
if k >= _min - 1:
    print(_min)
    return
gcd = 2
for i in range(_min, 1, -1):
    div = True
    j = 2 * i
    comp = i - k
    while div:
        if j - 1 <= _max:
            div = accum[j - 1] == accum[j - comp]
        elif j - comp <= _max:
            div = accum[_max] == accum[j - comp]
        else:
            break
        j += i
    if div:
        gcd = i
        break

print(gcd)

# 1494021276904
