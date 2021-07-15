FRUIT_NAMES = {'blueberry', 'pear', 'durian', 'ginkgo', 'peach', 'apple', 'cantaloupe', 'fig', 'mangosteen', 'watermelon', 'pineapple', 'cherry', 'pomegranate', 'carambola', 'hawthorn', 'persimmon', 'apricot', 'plum', 'litchi', 'mango', 'jujube', 'lemon', 'orange', 'tomato', 'banana', 'coconut', 'grape', 'pitaya'}
from itertools import chain

def cut_fruits(fruits):
    return list(chain(*map(cut,fruits)))

def cut(f):
    if f not in FRUIT_NAMES:
        yield f
    else:
        i = sum(divmod(len(f),2))
        yield f[:i]
        yield f[i:]
