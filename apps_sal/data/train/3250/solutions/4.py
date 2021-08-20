from re import compile
from functools import partial
short_form = partial(compile('(?i)(?<!^)[aeiou](?!$)').sub, '')
