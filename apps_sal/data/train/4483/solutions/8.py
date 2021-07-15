FRUIT_NAMES = {'blueberry', 'pear', 'durian', 'ginkgo', 'peach', 'apple', 'cantaloupe', 'fig', 'mangosteen', 'watermelon', 'pineapple', 'cherry', 'pomegranate', 'carambola', 'hawthorn', 'persimmon', 'apricot', 'plum', 'litchi', 'mango', 'jujube', 'lemon', 'orange', 'tomato', 'banana', 'coconut', 'grape', 'pitaya'}
from itertools import *
from math import *
def cut_fruits(fruits):
    def half(f):
        return [f[0:ceil(len(f)/2)], f[ceil(len(f)/2):]] if f in FRUIT_NAMES else [f]

    return list( chain(*[half(f) for f in fruits]) )
