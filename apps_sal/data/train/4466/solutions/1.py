example_text = r"""
//*    **    ****   ****  **  ** ******  *\n
//*   ***   **  ** **  ** **  ** **      *\n
//*  * **      **     **  **  ** *****   *\n
//*    **     **      **   *****     **  *\n
//*    **    **    **  **     **     **  *\n
//*  ****** ******  ****      ** *****   *\n
//@     @@  @@@@@@  @@@@   @@@@   @@@@   @\n
//@    @@   @@  @@ @@  @@ @@  @@ @@  @@  @\n
//@   @@@@     @@   @@@@  @@  @@ @@  @@  @\n
//@  @@  @@   @@    @@@@   @@@@  @@  @@  @\n
//@  @@  @@  @@    @@  @@   @@   @@  @@  @\n
//@   @@@@   @@     @@@@   @@     @@@@   @\n
"""
example_text = [
    l[5:-4]
    for l in example_text.replace('@', '*').split('\n')
    if l.strip()
]
SUPER_DIGITS = []
for super_line in [example_text[:6], example_text[6:]]:
    for i in range(5):
        SUPER_DIGITS.append([line[i * 7:(i + 1) * 7] for line in super_line])
SUPER_DIGITS.insert(0, SUPER_DIGITS.pop(-1))


def print_number(number, char):
    digits = str(number).rjust(5, '0')

    lines = ['' for _ in range(6)]
    for d in digits:
        for i in range(6):
            lines[i] += SUPER_DIGITS[int(d)][i]

    lines = [f'  {l} ' for l in lines]
    width = len(lines[0])
    lines.insert(0, '*' * width)
    lines.insert(1, ' ' * width)
    lines.append(' ' * width)
    lines.append('*' * width)
    lines = [f'*{l}*' for l in lines]
    return '\n'.join(lines).replace('*', char)
