def solve(s):
    """
    result = ''
    for char in s: 
        if char in '0123456789': 
            result += char
        else: 
            result += ' '
    return max(int(x) for x in result.split())
    """

    return max(int(x) for x in ''.join(c if c in '0123456789' else ' ' for c in s).split())

