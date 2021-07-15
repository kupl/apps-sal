def reverse_in_parentheses(s):
    stack = []
    for i in s:
        stack.append(i)
        
        if i == ')':
            opening = len(stack) - stack[::-1].index('(') - 1
            stack.append(''.join([i[::-1].translate(str.maketrans('()',')(')) for i in stack[opening:][::-1]]))  
            del stack[opening:-1]
  
    return ''.join(stack)  
