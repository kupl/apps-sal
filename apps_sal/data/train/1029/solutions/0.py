T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    completed = list(map(int, input().split()))
    jobs = []
    for i in range(1, n + 1):
        if i not in completed:
            jobs.append(i)
    jobs.sort()
    chef = []
    ass = []
    for i in range(len(jobs)):
        if i % 2 == 0:
            chef.append(str(jobs[i]))
        else:
            ass.append(str(jobs[i]))
    print(' '.join(chef))
    print(' '.join(ass))
