import re, itertools

WORDING = dict(map(lambda x: x.split(" | "),"""
- | *p -= %s;
+ | *p += %s;
< | p -= %s;
> | p += %s;
[ | if (*p) do {
] | } while (*p);
. | putchar(*p);
, | *p = getchar();
""".splitlines()[1:]))

def brainfuck_to_c(source_code):
    code, old_code = source_code, ""
    while (code != old_code):
        old_code = code
        code = re.sub("[^\+\-\<\>\[\]\.\,]+|\+\-|\-\+|\<\>|\>\<|\[\]", "", code)
    indent, output = 0, []
    for command, sequence in itertools.groupby(code):
        repeat = len(list(sequence))
        if command in "+-<>":
            output += [indent * " " + WORDING[command] % repeat]
        if command in ".,[]":
            for i in range(repeat):
                indent -= 2 * (command is "]")
                output += [indent * " " + WORDING[command]]
                indent += 2 * (command is "[")
        if indent < 0:
            break
    return "Error!" if indent else "\n".join(output + [""])
