def produce(n):
    x = 300
    for i in range(n):
        yield x
        x = int(x * 0.8)

def egged(year, span):
    if year == 0:
        return 'No chickens yet!'
    return sum(produce(min(year, span))) * 3
