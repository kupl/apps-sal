def enough(cap, on, wait):
    # Your code here
    cap -= on
#     if cap>=wait:
#         return 0
#     else:
#         return wait-cap
    return max(wait - cap, 0)
