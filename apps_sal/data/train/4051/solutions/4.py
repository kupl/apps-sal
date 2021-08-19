from functools import partial
from re import compile
toUnderScore = partial(compile('(?<=[a-zA-Z])(?=[A-Z0-9])|(?<=[0-9])(?=[A-Z])').sub, '_')
