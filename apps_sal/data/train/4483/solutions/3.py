FRUIT_NAMES = {'blueberry', 'pear', 'durian', 'ginkgo', 'peach', 'apple', 'cantaloupe', 'fig', 'mangosteen', 'watermelon', 'pineapple', 'cherry', 'pomegranate', 'carambola', 'hawthorn', 'persimmon', 'apricot', 'plum', 'litchi', 'mango', 'jujube', 'lemon', 'orange', 'tomato', 'banana', 'coconut', 'grape', 'pitaya'}
from math import ceil

def cut_fruits(fruits):
    result = []
    for x in fruits:
        if x in FRUIT_NAMES:
            result.append(x[:ceil(len(x)/2)])
            result.append(x[ceil(len(x)/2):])
        else:
            result.append(x)
    return result

