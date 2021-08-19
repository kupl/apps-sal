import re


def brainfuck_to_c(source):
    source = re.sub('[^+-<>,.\\[\\]]', '', source)
    before = ''
    while source != before:
        before = source
        source = re.sub('\\+-|-\\+|<>|><|\\[\\]', '', source)
    braces = re.sub('[^\\[\\]]', '', source)
    while braces.count('[]'):
        braces = braces.replace('[]', '')
    if braces:
        return 'Error!'
    commands = re.findall('\\++|-+|>+|<+|[.,\\[\\]]', source)
    output = []
    indent = 0
    for cmd in commands:
        if cmd[0] in '+-<>':
            line = '%sp %s= %s;\n' % ('*' if cmd[0] in '+-' else '', '+' if cmd[0] in '+>' else '-', len(cmd))
        elif cmd == '.':
            line = 'putchar(*p);\n'
        elif cmd == ',':
            line = '*p = getchar();\n'
        elif cmd == '[':
            line = 'if (*p) do {\n'
        elif cmd == ']':
            line = '} while (*p);\n'
            indent -= 1
        output.append('  ' * indent + line)
        if cmd == '[':
            indent += 1
    return ''.join(output)
