def uniq_c(seq): 
    stack, out = [], []
    for x in seq:
        if stack and x == stack[-1]:
            stack.append(x)
        else:
            if stack:
                out.append( (stack[-1], len(stack)) )
                stack.clear()
                stack.append(x)
            else:
                stack.append(x)
    
    return stack and out + [ (stack[-1], len(stack)) ] or out

