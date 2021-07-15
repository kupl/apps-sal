def enough(cap, on, wait):
    return -min(0, cap-(on+wait))
