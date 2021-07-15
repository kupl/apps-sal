import re
reverse_words = lambda s: ''.join([i[::-1] for i in re.split(r'(\s+)', s)]) 
