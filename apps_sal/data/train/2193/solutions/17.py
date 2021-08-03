n = int(input())
score = []
son = 0
for i in range(n):
    wk1 = sum([*list(map(int, input().split()))])
    if (i == 0):
        son = wk1
    score.append(wk1)
score.sort(reverse=True)
print(score.index(son) + 1)
