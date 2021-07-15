def uni_total(string):
    int = [ord(x) for x in string]
    sum = 0
    for i in int:
        sum += i
    return sum
