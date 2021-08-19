import re
from functools import partial
apparently = partial(re.sub, '(?<=\\b(and|but)\\b(?! apparently\\b))', ' apparently')
