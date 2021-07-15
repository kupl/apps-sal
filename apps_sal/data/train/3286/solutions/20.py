def enough(cap, on, wait):
    answer = on + wait - cap
    if answer < 0:
        return 0
    else:
        return answer
