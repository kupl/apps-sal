n = int(input())
strengths = list(map(int, input().split()))
strengths.sort(reverse=True)
summ = 0
for i in range(0, len(strengths)):
    summ += strengths[i] * (len(strengths) - 2 * (i + 1) + 1)
print(summ)
