def interpreter(code, tape):

    p, tapeP, tape = 0, 0, list(tape)
    
    stack, bracketMove = [], {}
    for i,c in enumerate(code):
        if c == '[': stack.append(i)
        elif c == ']':
          bracketMove[i] = stack[-1]
          bracketMove[stack.pop()] = i
    
    while p < len(code) and 0 <= tapeP < len(tape):
        if   code[p] == "*":                            tape[tapeP] = "0" if tape[tapeP] == "1" else "1"
        elif code[p] == "<":                            tapeP -= 1
        elif code[p] == ">":                            tapeP += 1
        elif (code[p] == "[" and tape[tapeP] == "0") \
             or (code[p] == "]" and tape[tapeP] != "0"):  p = bracketMove[p]
        p += 1
    
    return "".join(tape)
