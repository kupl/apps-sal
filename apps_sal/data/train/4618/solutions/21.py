
def positive_sum(n):
    b = 0
    if not n:
        return 0
    else:
        for i in range(len(n)):
            if n[i] < 0:
                pass
            else:
                b += n[i]
        return b
