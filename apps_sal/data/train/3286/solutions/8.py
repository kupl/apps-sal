def enough(cap, on, wait):
    res = cap-(on+wait)
    return [0, abs(res)][res<0]
