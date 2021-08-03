from math import ceil
FRUIT_NAMES = {'blueberry', 'pear', 'durian', 'ginkgo', 'peach', 'apple', 'cantaloupe', 'fig', 'mangosteen', 'watermelon', 'pineapple', 'cherry', 'pomegranate', 'carambola', 'hawthorn', 'persimmon', 'apricot', 'plum', 'litchi', 'mango', 'jujube', 'lemon', 'orange', 'tomato', 'banana', 'coconut', 'grape', 'pitaya'}


def cut_fruits(fruits):
    res = []
    for fruit in fruits:
        if fruit in FRUIT_NAMES:
            med = ceil(len(fruit) / 2)
            res.extend([fruit[: med], fruit[med:]])
        else:
            res.append(fruit)
    return res
