n = int(input())
l = list(map(int, input().strip().split()))
even = [0 for i in range(2**21)]
odd = [0 for i in range(2**21)]
cur = 0
even[0] = 1
for i in range(n):
    cur = cur^l[i]
    if i%2:
        even[cur] += 1
    else:
        odd[cur] += 1
ans = 0
for i in range(2**21):
    if even[i] >= 2: ans += (even[i]*(even[i]-1))/2
    if odd[i] >= 2: ans += (odd[i]*(odd[i]-1))/2
print(int(ans))

