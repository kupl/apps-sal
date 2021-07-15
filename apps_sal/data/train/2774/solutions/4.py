def is_balanced(source, caps):
    matches = dict([(b,a) for a,b in zip(caps[::2],caps[1::2]) ])
    source = [char for char in source if char in caps]
    stack = []
    for char in source:
        if len(stack) == 0: stack.append(char)
        elif matches.get(char) == stack[-1]: del stack[-1]
        else: stack.append(char)
    return len(stack) == 0
