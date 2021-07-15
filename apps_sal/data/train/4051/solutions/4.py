from functools import partial
from re import compile

toUnderScore = partial(compile(r"(?<=[a-zA-Z])(?=[A-Z0-9])|(?<=[0-9])(?=[A-Z])").sub, r"_")
