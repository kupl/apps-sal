def brainfuck_to_c(source_code):
    result = ''
    possible = '+-<>,.[]'
    spacing = 0
    braces_count = 0
    op_count = 0
    source_code = ''.join(letter for letter in source_code if letter in possible)
    while '[]' in source_code or '+-' in source_code or '<>' in source_code or '-+' in source_code or '><' in source_code:
        source_code = source_code.replace('[]','').replace('+-','').replace('<>','').replace('-+','').replace('><','')
    if source_code.count('[') != source_code.count(']'):
        return 'Error!'
    for index,letter in enumerate(source_code):
        if letter == '[':
            braces_count += 1
            result += ' ' * spacing + 'if (*p) do {\n'
            spacing += 2
        elif letter == ']':
            braces_count -= 1
            if braces_count < 0:
                return 'Error!'
            spacing -= 2
            result += ' ' * spacing + '} while (*p);\n'
        elif letter == '+' or letter == '-':
            if index < len(source_code) - 1 and source_code[index + 1] == letter:
                op_count += 1
                continue
            else:
                result += ' ' * spacing + f'*p {letter}= {op_count + 1};\n'
                op_count = 0
        elif letter == '<' or letter == '>':
            if index < len(source_code) - 1 and source_code[index + 1] == letter:
                op_count += 1
                continue
            else:
                equi = '+' if letter == '>' else '-'
                result += ' ' * spacing + f'p {equi}= {op_count + 1};\n'
                op_count = 0
        elif letter == '.':
            result += ' ' * spacing + 'putchar(*p);\n'
        elif letter == ',':
            result += ' ' * spacing + '*p = getchar();\n'
    if braces_count != 0:
        return 'Error!'
    return result
