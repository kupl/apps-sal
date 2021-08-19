test_cases = int(input())
for i in range(test_cases):
    chefList = []
    assistantList = []
    (n, m) = map(int, input().split())
    jobsCompleted = set(map(int, input().split()))
    totalJobs = set(range(1, n + 1))
    remainingJobs = list(totalJobs - jobsCompleted)
    remainingJobs.sort()
    for j in range(len(remainingJobs)):
        if j % 2 == 0:
            chefList.append(remainingJobs[j])
        else:
            assistantList.append(remainingJobs[j])
    print(*chefList)
    print(*assistantList)
