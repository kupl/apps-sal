def to_alternating_case(s):
    return ''.join(c.upper() if c.islower() else c.lower() if c.isupper() else c for c in s)

    # Less compact version of above:
    #
    # a = ''
    # for c in s:
    #     if c.islower():
    #         a += c.upper()
    #     elif c.isupper():
    #         a += c.lower()
    #     else:
    #         a += c
    # return a
