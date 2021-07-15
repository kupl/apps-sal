N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

low = [A[0]]
high = [A[N-1]]
for i in range(1, N):
    low.append(min(A[i], low[i-1]))
for i in reversed(list(range(N-1))):
    high.append(max(A[i], high[N-2-i]))

high.reverse()
max_gap = max([high[i] - low[i] for i in range(N)])
num = 0
first = True
for i in range(N):
    if high[i] - low[i] == max_gap:
        if first:
            idx = i
            num += 1
            first = False
        else:
            if low[idx] != low[i]:
                idx = i
                num += 1

print(num)

