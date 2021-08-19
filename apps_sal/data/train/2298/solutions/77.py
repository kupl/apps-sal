(N, T) = map(int, input().split())
(*A,) = map(int, input().split())
min_price = A[0]
max_prof = 0
count = 1
for a in A[1:]:
    prof = a - min_price
    if prof < 0:
        min_price = a
    elif prof == max_prof:
        count += 1
    elif prof > max_prof:
        max_prof = prof
        count = 1
print(count)
