from itertools import groupby
import re
def brainfuck_to_c(sc):
    sc = remove(sc,sc)
    bracket, space, code = [], '', ''
    for i, j in groupby(sc):
        n = len(list(j))
        if i in '-+' :   code += space + f"*p {'+-'[i=='-']}= {n};\n"
        elif i in '<>' : code += space + f"p {'+-'[i=='<']}= {n};\n"
        elif i == '.' :  code += (space+'putchar(*p);\n')*n
        elif i == ',' :  code += (space+"*p = getchar();\n")*n
        elif i == '[':
            for n in range(n):
                code += space + 'if (*p) do {\n'
                space += '  '
                bracket.append('[')
        elif i == ']':
            for n in range(n):
                if not bracket or bracket.pop() != '[':return 'Error!'
                space = space[:-2]
                code += space + '} while (*p);\n'
    return 'Error!' if bracket else code

def remove(prev,sc):
    sc = re.sub(r'\[\]','', re.sub(r'<>|><','', re.sub(r'\+-|-\+','', re.sub(r'[^\+-<>,.\[\]]','',sc))))
    return sc if sc==prev else remove(sc,sc)
