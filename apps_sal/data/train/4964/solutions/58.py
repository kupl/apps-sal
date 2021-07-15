def is_uppercase(inp):

    for i in range(len(inp)):
        ascii = ord(inp[i])
        if (97 <= ascii <= 122):

            return False

    return True

