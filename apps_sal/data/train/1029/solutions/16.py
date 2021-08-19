T = int(input())
for i in range(T):
    (n, m) = map(int, input().split())
    jobsList = []
    for j in range(n):
        jobsList.append(j + 1)
    jobsDone = list(map(int, input().split()))
    for k in range(m):
        jobsList.remove(jobsDone[k])
    l = 0
    p = 1
    jobsA = []
    jobsB = []
    while l < len(jobsList):
        jobsA.append(jobsList[l])
        l += 2
    while p < len(jobsList):
        jobsB.append(jobsList[p])
        p += 2
    for q in range(len(jobsA)):
        print(jobsA[q], end=' ')
    print()
    for r in range(len(jobsB)):
        print(jobsB[r], end=' ')
    print()
