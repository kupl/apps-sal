def grader(s): return 'FDCBAF'[sum((s >= 0.6, s >= 0.7, s >= 0.8, s >= 0.9, s > 1))]
