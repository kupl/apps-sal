def day_plan(h, t, d): return t * d > h * 60 and "You're not sleeping tonight!" or ([(h * 60 - t * d) // (t - 1 + 1e-9), d] * t)[1:]
