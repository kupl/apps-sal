def enough(cap, on, wait):
    if cap - on == wait:
        return 0
    elif cap - on < wait:
        return (cap - on - wait) * (-1)
    elif wait < cap - on:
        return 0
