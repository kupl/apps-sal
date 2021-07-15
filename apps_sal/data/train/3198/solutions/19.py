def check_exam(*arr):
    return max(0, sum([-1, 4][a==b] if b else 0 for a,b in zip(*arr)))
