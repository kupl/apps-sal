enough = lambda cap, on, wait: 0 if cap - on - wait >= 0 else abs(cap - on - wait)
