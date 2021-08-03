import math


def ceil(value, step):
    return math.ceil(value / step) * step


def floor(value, step):
    return math.floor(value / step) * step


def roundRobin(jobs, frame, index):
    for i in range(index):
        jobs[i] = min(jobs[i], ceil(jobs[index], frame))
    for i in range(index + 1, len(jobs)):
        jobs[i] = min(jobs[i], floor(jobs[index] - 1, frame))
    return sum(jobs)
