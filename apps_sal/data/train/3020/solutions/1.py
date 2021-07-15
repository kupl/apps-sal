from re import sub
from functools import partial
kontti = partial(sub, r'(?i)(\S*?[aeiouy])(\S*)', r'ko\2-\1ntti')
