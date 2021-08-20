(N, T) = map(int, input().split())
(*A,) = map(int, input().split())
max_price = A[N - 1]
max_prof = 0
count = 1
for a in reversed(A[:N - 1]):
    prof = max_price - a
    if prof < 0:
        max_price = a
    elif prof == max_prof:
        count += 1
    elif prof > max_prof:
        max_prof = prof
        count = 1
print(count)
