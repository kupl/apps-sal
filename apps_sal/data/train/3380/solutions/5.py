import re
def look_and_say_sequence(element, n):
    return element if n == 1 else look_and_say_sequence(''.join(f'{len(e.group())}{e.group(1)}' for e in re.finditer(r'(\d)\1*',element)), n-1)
