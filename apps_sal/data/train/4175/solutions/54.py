def repeater(string, n):
    new_string = ""

    while n != 0:
        new_string += string
        n -= 1

    return new_string

    # Your code goes here.
