import re
def calculate(expression):
    if re.search(r'[^\.0123456789+\-*$]', expression): return '400: Bad request'
    if re.match('^(?:\d+\.)?\d+$', expression): return float(expression)
    return (
        (
            lambda m:
                (lambda x, o, y: ({ '+': x + y, '-': x - y, '*': x * y, '$': x / y })[o])
                (calculate(m.group(1)), m.group(2), calculate(m.group(3)))
                if m else 0
        )
        (re.search('(.+)([+-])(.+)', expression) or re.search('(.+)([*$])(.+)', expression))
    )

