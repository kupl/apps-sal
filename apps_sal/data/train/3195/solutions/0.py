brackets = {"}":"{","]":"[",")":"("}

def braces_status(s):
    stack = []
    
    for c in s:
        if c in "[({":
            stack.append(c)
        elif c in "])}":
            if not stack or stack.pop() != brackets[c]:
                return False
    
    return not stack
