import re


def increment_string(strng):
    pattern = re.compile(r'[0-9]+')
    match = re.findall(pattern, strng)
    print(strng)

    if match:
        found = match[-1]
        length = len(found)
        add = str(int(found) + 1)
        changed = add.zfill(length)
        modified = strng.replace(found, changed)
    else:
        modified = strng + '1'
    return modified
