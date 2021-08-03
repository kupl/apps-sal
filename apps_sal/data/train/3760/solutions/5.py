def roundRobin(jobs, slice, index):
    num_slices = (jobs[index] + slice - 1) // slice
    before = num_slices * slice
    after = (num_slices - 1) * slice
    return sum(min(before, cc) for cc in jobs[0:index]) \
        + sum(min(after, cc) for cc in jobs[index + 1:]) + jobs[index]
