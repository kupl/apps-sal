import re
from functools import partial

apparently = partial(re.sub, r'(?<=\b(and|but)\b(?! apparently\b))', ' apparently')
