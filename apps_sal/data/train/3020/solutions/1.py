from re import sub
from functools import partial
kontti = partial(sub, '(?i)(\\S*?[aeiouy])(\\S*)', 'ko\\2-\\1ntti')
