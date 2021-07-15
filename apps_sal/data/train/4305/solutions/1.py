def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum

def order_weight(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))
    
    return result
