def balanced_parens(n):
    '''
    To construct all the possible strings with n pairs of balanced parentheses 
    this function makes use of a stack of items with the following structure:
        (current, left, right)
    Where:
        current is the string being constructed
        left is the count of '(' remaining
        right is the count of  ')' remaining
    '''
    stack = [('', n, 0)]
    result = []

    # Loop until we run out of items in the stack
    while stack:
        current, left, right = stack.pop()

        # if no '(' or ')' left to add, add current to the result
        if left == 0 and right == 0:
            result.append(current)

        # if we can, add a '(' and return to the stack
        if left > 0:
            stack.append((current + '(', left - 1, right + 1))

        # if we can, add a ')' and return to the stack
        if right > 0:
            stack.append((current + ')', left, right - 1))

    return result
