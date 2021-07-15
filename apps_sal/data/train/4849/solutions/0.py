import re
def my_very_own_split(string, delimiter = None):
    if delimiter == '': raise ValueError('empty delimiter')
    if delimiter == None: delimiter = '\s+'
    else: delimiter = re.escape(delimiter)
    pos = 0
    for m in re.finditer(delimiter, string):
        yield string[pos:m.start()]
        pos = m.end()
    yield string[pos:]

