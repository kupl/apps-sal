def pop(tape, pc, out, stack):
    pc += 1
    stack.pop()
    return pc, out, stack

def zstack(tape, pc, out, stack):
    pc += 1
    stack.append(0)
    return pc, out, stack

def inc(tape, pc, out, stack):
    pc += 1
    stack[-1] += 1
    if stack[-1] > 255: stack[-1] = 0
    return pc, out, stack

def dec(tape, pc, out, stack):
    pc += 1
    stack[-1] -= 1
    if stack[-1] < 0: stack[-1] = 255
    return pc, out, stack

def ascii(tape, pc, out, stack):
    pc += 1
    out += chr(stack[-1])
    return pc, out, stack

def skip(tape, pc, out, stack):
    pc += 1
    if stack[-1] == 0:
        c = tape[pc]
        while c != "]":
            pc += 1
            c = tape[pc]
        pc += 1
    return pc, out, stack

def back(tape, pc, out, stack):
    #return None
    if stack[-1] != 0:
        pc -= 1
        c = tape[pc]
        while c != "[":
            pc -= 1
            c = tape[pc]
        pc += 1
    else:
        pc += 1
    return pc, out, stack

dispatch = {
    "^": pop,
    "!": zstack,
    "+": inc,
    "-": dec,
    "*": ascii,
    "[": skip,
    "]": back,
}

def interpreter(tape):
    out = ""
    stack = [0]
    pc = 0
    c = tape[pc]
    while c:
        if c in dispatch:
            pc, out, stack = dispatch[c](tape, pc, out, stack)
        else:
            pc += 1
        c = tape[pc: pc + 1]
    return out
    # Happy Coding! :)

