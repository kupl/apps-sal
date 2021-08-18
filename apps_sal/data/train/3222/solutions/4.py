
def get_sum(a, b):
    x = 0
    if a == b:
        return a

    elif a > b:
        for i in range(b, a + 1):
            x += i
    elif b > a:
        for i in range(a, b + 1):
            x += i
    return x
