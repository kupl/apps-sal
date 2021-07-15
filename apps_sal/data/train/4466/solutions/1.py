# Build digit templates from the given examples in the instructions
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
# Clean/standardise the source text
example_text = [
    l[5:-4] 
    for l in example_text.replace('@', '*').split('\n') 
    if l.strip()
]
# Extract the 7x6 super digits
SUPER_DIGITS = []
for super_line in [example_text[:6], example_text[6:]]:
    for i in range(5):
        SUPER_DIGITS.append([line[i * 7:(i + 1) * 7] for line in super_line])
# Move the 0 from the end to start
SUPER_DIGITS.insert(0, SUPER_DIGITS.pop(-1))


def print_number(number, char): 
    # Pad to 5 digits
    digits = str(number).rjust(5, '0')
    
    # Add the digits (each one has a trailing space)
    lines = ['' for _ in range(6)]
    for d in digits:
        for i in range(6):
            lines[i] += SUPER_DIGITS[int(d)][i]
    
    # Justify
    lines = [f'  {l} ' for l in lines]
    width = len(lines[0])
    # Add header
    lines.insert(0, '*' * width)
    lines.insert(1, ' ' * width)
    # Add footer
    lines.append(' ' * width)
    lines.append('*' * width)
    # Add border
    lines = [f'*{l}*' for l in lines]
    # Concatenate and substitute
    return '\n'.join(lines).replace('*', char)

