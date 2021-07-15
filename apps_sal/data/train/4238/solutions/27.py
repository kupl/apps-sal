squares_needed=lambda n: 1+squares_needed(n>>1) if n else n
