def enough(cap, on, wait):
    
    remaining = cap - (on+wait)
    return abs(remaining) if remaining < 0 else 0
