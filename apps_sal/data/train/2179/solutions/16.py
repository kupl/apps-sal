(a, b, c) = [int(x) for x in input().split()]
n = int(input())
banknotes = [int(x) for x in input().split()]
res = 0
for note in banknotes:
    if note > b and note < c:
        res += 1
print(res)
