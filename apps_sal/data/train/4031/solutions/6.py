def interpreter(code, tape):
    cells = list(map(int, tape))
    cell_p, command_p = 0, -1
    scope_stack = [(0, len(code))]
    while True:
        command_p += 1
        if command_p >= len(code) or cell_p >= len(cells) or cell_p < 0: break
        command = code[command_p]
        if command == '>': cell_p += 1
        elif command == '<': cell_p -= 1
        elif command == '*': cells[cell_p] = int(not cells[cell_p])
        elif command == '[':
            scope_end_p = code.rfind(']', scope_stack[-1][0], scope_stack[-1][1])
            if not cells[cell_p]: command_p = scope_end_p
            else: scope_stack.append((command_p, scope_end_p))
        elif command == ']': 
            if cells[cell_p]: command_p = scope_stack[-1][0]
            else: scope_stack.pop()
    return ''.join(list(map(str, cells)))

