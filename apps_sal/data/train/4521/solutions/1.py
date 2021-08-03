def numberOfSteps(steps, m):
    return next((n for n in range((steps + 1) // 2, steps + 1) if n % m == 0), -1)
