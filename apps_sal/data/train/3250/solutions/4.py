from re import compile
from functools import partial

short_form = partial(compile(r"(?i)(?<!^)[aeiou](?!$)").sub, "")
