from functools import partial
from re import compile
s = "[\\w'-]"
x = f'(?<!{s})'
y = f'(?!{s})'
conv1 = partial(compile(f'{s}{{7,}}|{s}*[tT]{s}*[tT]{s}*').sub, lambda x: x.group()[::-1])
conv2 = partial(compile(f'{x}({s}{s}{y}|{s}{{1,6}}(?=,))').sub, lambda x: x.group().upper())
conv3 = partial(compile(f'{x}\\w{y}(?!,)').sub, '0')


def spin_solve(sentence):
    return conv3(conv2(conv1(sentence)))
