import re
def reverse_words(s): return ''.join([i[::-1] for i in re.split(r'(\s+)', s)])
