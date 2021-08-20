import re


def brainfuck_to_c(source_code):
    s = re.findall('[\\+-<>\\[\\]\\.,]+', source_code)
    s = ''.join(s)
    pattern = re.compile('<>|><|\\+-|-\\+|\\[\\]')
    while True:
        l = len(s)
        s = pattern.sub('', s)
        if l == len(s):
            break
    depth = 0
    for i in s:
        if i == '[':
            depth += 1
        if i == ']':
            depth -= 1
        if depth < 0:
            return 'Error!'
    if depth != 0:
        return 'Error!'
    s = re.findall('\\++|\\-+|<+|>+|\\.|,|\\[|\\]', s)
    for i in range(len(s)):
        if re.match('\\++', s[i]):
            s[i] = ' ' * depth + '*p += ' + str(len(s[i])) + ';\n'
        if re.match('-+', s[i]):
            s[i] = ' ' * depth + '*p -= ' + str(len(s[i])) + ';\n'
        if re.match('>+', s[i]):
            s[i] = ' ' * depth + 'p += ' + str(len(s[i])) + ';\n'
        if re.match('<+', s[i]):
            s[i] = ' ' * depth + 'p -= ' + str(len(s[i])) + ';\n'
        if re.match('\\.+', s[i]):
            s[i] = ' ' * depth + 'putchar(*p);\n'
        if re.match(',+', s[i]):
            s[i] = ' ' * depth + '*p = getchar();\n'
        if s[i] == '[':
            s[i] = ' ' * depth + 'if (*p) do {\n'
            depth += 2
        if s[i] == ']':
            depth -= 2
            s[i] = ' ' * depth + '} while (*p);\n'
    s = ''.join(s)
    return s
