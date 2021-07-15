def is_odd(num):
    """ Returns True if number is odd and False otherwise """
    return not int(num) % 2 == 0

def insert_dash(num):
    """ insert_dash() inserts dashes between each pair of odd numbers
        and returns it.
    """
    num_str = str(num)
    new_str = num_str[0]
    for i in range(1, len(num_str)):
        if is_odd(num_str[i]) and is_odd(num_str[i - 1]):
            new_str += ("-" + num_str[i])
        else:
            new_str += num_str[i]
    return new_str
