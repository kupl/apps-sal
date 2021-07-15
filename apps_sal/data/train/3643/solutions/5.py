def distribute(nodes, workload):
    jobs_per_server, remaining = divmod(workload, nodes)
    jobs, start = [], 0
    for _ in range(nodes):
        how_many = jobs_per_server + (remaining > 0)
        jobs.append(list(range(start, start + how_many)))
        start += how_many
        remaining -= 1
    return jobs
