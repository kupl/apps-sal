from functools import partial
from re import compile
ka_co_ka_de_ka_me = partial(compile('(?i)^|(?<=[aeiou])(?![aeiou]|$)').sub, 'ka')
