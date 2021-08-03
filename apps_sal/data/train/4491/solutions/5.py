def solve(left, right):
    result = ''
    for char in left:
        if char not in right:
            result += char
    for char in right:
        if char not in left:
            result += char
    return result
