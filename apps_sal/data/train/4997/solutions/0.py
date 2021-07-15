cache = {}
def sum_div(x):
    if x not in cache:
        cache[x] = sum(i for i in range(1, x+1) if x % i == 0)
    return cache[x]

def is_required(x):
    reversed = int(str(x)[::-1])
    return x != reversed and sum_div(x) == sum_div(reversed)

required = [x for x in range(528, 10**4) if is_required(x)]

def equal_sigma1(nMax):
    return sum(x for x in required if x <= nMax)

