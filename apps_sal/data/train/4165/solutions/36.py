def uni_total(string):
    accumulator = 0
    for eachchar in string:
        accumulator = accumulator + ord(eachchar)
    return accumulator
