def calculate_probability(n):
    # your code here
    if n == 0 or n == 1:
        return 0
    elif n >= 365:
        return 1
    else:
        t = 365**n
        s = 1
        c = 0
        while c < n:
            s *= 365 - c
            c += 1
        return float('{:.2f}'.format((t - s) / t))
