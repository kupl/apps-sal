# Takes any input and reverses the digits. Preserves sign.

def reverse_number(number):
    if number >= 0:
        return int(str(number)[::-1])
    else:
        return -int(str(number)[:0:-1])
