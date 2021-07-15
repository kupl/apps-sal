from itertools import zip_longest
combine_strings = lambda *strings: ''.join(map(''.join, zip_longest(*strings, fillvalue='')))
