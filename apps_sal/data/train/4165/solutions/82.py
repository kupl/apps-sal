def uni_total(string):
    # your code here
    sum = 0
    for e in string:
        sum = sum + ord(e)
    return sum
