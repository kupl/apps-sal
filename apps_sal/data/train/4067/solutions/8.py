def iq_test(numbers):
    all = numbers.split(" ")
    odd = [int(x) for x in all if int(x) % 2 != 0]
    even = [int(x) for x in all if int(x) % 2 == 0]
    if len(odd) == 1:
        return all.index(str(odd[0])) + 1
    return all.index(str(even[0])) + 1
