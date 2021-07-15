import re

def word_wrap(text, limit):
    r = fr'\s*(.{{1,{limit}}}((?<=\w)(?!\w)|(?=\w+(?<=\w{{{limit+1}}})))|\w{{{limit}}})'
    return '\n'.join(m.group(1) for m in re.finditer(r, text))
