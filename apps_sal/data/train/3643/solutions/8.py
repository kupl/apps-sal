def distribute(nodes, workload):
    n = workload // nodes
    r = workload % nodes
    jobs = []
    works = [i for i in range(workload)]
    j = 0
    for i in range(nodes):
        if i < r:
            jobs.append([works.pop(0) for i in range(n+1)])
        else:
            jobs.append([works.pop(0) for i in range(n)])
    return jobs
