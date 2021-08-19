def encode(message, key):
    # initialize variables
    output = []
    i = 0

    # convert key to a list of integers
    key = [int(d) for d in str(key)]

    # encode characters in 'message'
    for char in message:
        n = ord(char) + key[i]
        output.append(n - 96)
        i = (i + 1) % len(key)

    # return the results
    return output
