def round_to_next5(n):
    # Your code here
    import math

    if n <= 0 and n > -5:
        output = 0
    elif n <= -5:
        output = math.ceil(n / 5) * 5
    else:
        output = math.ceil(n / 5) * 5
    return output
