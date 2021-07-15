def iq_test(numbers):
    eo = [int(n)%2 for n in numbers.split()]
    return eo.index(1 if eo.count(0)>1 else 0)+1
