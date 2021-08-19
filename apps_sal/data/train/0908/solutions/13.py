import bisect
comb = [0] * 100001
comb[1] = 1
for i in range(1, 100001):
    comb[i] = comb[i - 1] + i
for _ in range(eval(input())):
    n = eval(input())
    index = bisect.bisect_left(comb, n)
    if comb[index] == n:
        print(index)
    else:
        print(index - 1)
