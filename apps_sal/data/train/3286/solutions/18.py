def enough(cap, on, wait):
    # Your code here
    import math
    if cap >= (on + wait):
        return 0
    elif cap < (on + wait):
        return abs((cap - (wait + on)))
