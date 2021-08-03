n, q = map(int, input().split())
A = list(map(int, input().split()))
sizes = dict()


for j in range(n):
    if A[j] in sizes:
        sizes[A[j]][2] += 1
        sizes[A[j]][1] = j
    else:
        sizes[A[j]] = [j, j, 1]
# print(sizes)

answer = 0
end = -1
max_size = -1
for j in range(n):
    end = max(end, sizes[A[j]][1])
    max_size = max(max_size, sizes[A[j]][2])
    if j == end:
        answer += max_size
        #print(j, max_size)
        max_size = 0

answer = -answer

for j in sizes:
    answer += sizes[j][2]

print(answer)
