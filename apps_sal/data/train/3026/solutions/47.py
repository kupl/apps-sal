
def min_value(digits):
    # your code here
    
    set_digits = set()
    for digit in digits:
        set_digits.add(digit)
    sorted_digits = sorted(set_digits)
    interim = "".join((list(map(str,sorted_digits))))
    return int(interim)


