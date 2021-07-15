def reverse_in_parentheses(s):

    def find_pairs(s):
        stack, pairs = [], {}
        for i, c in enumerate(s):
            if c == '(': stack.append(i)
            if c == ')':
                opening = stack.pop()
                pairs[opening] = i
                pairs[i] = opening
        return pairs

    def walk(start, end, direction):
        while start != end:
            if s[start] not in '()':
                yield s[start]
            else:
                yield '('
                yield from walk(pairs[start]-direction, start, -direction)
                yield ')'
                start = pairs[start]
            start += direction
    
    pairs = find_pairs(s)
    return ''.join(walk(0, len(s), 1))
