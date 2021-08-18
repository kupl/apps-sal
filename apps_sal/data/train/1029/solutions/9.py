T = int(input())

while T:
    T -= 1
    totalJobs, completedJobs = map(int, input().split())
    iJobs = []
    cJobs = []
    chef = []
    assistant = []

    cJobs = [int(i) for i in input().split()]
    for i in range(1, totalJobs + 1):
        if i not in cJobs:
            iJobs.append(i)
    iJobs.sort()

    for i in range(len(iJobs)):
        if i % 2 == 0:
            chef.append(iJobs[i])
        else:
            assistant.append(iJobs[i])
    print(' '.join([str(i) for i in chef]))
    print(' '.join([str(i) for i in assistant]))
