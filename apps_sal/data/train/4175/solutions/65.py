def repeater(string, n):
    strin = string
    for i in range(1, n, 1):
        strin += string
    return strin
    # Your code goes here.
