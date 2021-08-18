def magic_call_depth_number(program):
    templates = dict()
    code = str()

    i = 0
    while i < len(program):

        if program[i] != 'p':
            code += program[i]
        else:
            i += 1
            n = str()
            while program[i].isdigit():
                n += program[i]
                i += 1

            template = str()
            while program[i] != 'q':
                template += program[i]
                i += 1

            templates[n] = template

        i += 1

    mymin = 999
    mymax = 0

    i = 0
    while i < len(code):
        while code[i] == 'F' or code[i] == 'L' or code[i] == 'R':
            i += 1
            while code[i].isdigit():
                i += 1

        i += 1
        n = str()
        while i < len(code) and code[i].isdigit():
            n += code[i]
            i += 1

        min_max = calc_min_max([n], n, templates, 0)
        mymin = min(mymin, min_max[0])
        mymax = max(mymax, min_max[1])

    if mymax == 0:
        mymin = 0

    return [mymin, mymax]


def calc_min_max(used, c, templates, depth):
    mymin = 999
    mymax = 0

    flag = 0
    i = 0
    while i < len(templates[c]):
        while i < len(templates[c]) and (templates[c][i] == 'F' or templates[c][i] == 'L' or templates[c][i] == 'R'):
            i += 1
            while i < len(templates[c]) and (templates[c][i].isdigit()):
                i += 1

        if not (i < len(templates[c])):
            break

        i += 1
        n = str()
        while i < len(templates[c]) and templates[c][i].isdigit():
            n += templates[c][i]
            i += 1

        flag = 1
        if used.count(n):
            loop_with_depth = depth + 1
            mymin = min(mymin, loop_with_depth)
            mymax = max(mymax, loop_with_depth)
        else:
            used_copy = used.copy()
            used_copy.append(n)
            min_max = calc_min_max(used_copy, n, templates, depth + 1)
            mymin = min(mymin, min_max[0])
            mymax = max(mymax, min_max[1])

    return [mymin if flag else 0, mymax]
