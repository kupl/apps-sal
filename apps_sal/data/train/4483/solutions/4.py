FRUIT_NAMES = {'blueberry', 'pear', 'durian', 'ginkgo', 'peach', 'apple', 'cantaloupe', 'fig', 'mangosteen', 'watermelon', 'pineapple', 'cherry', 'pomegranate', 'carambola', 'hawthorn', 'persimmon', 'apricot', 'plum', 'litchi', 'mango', 'jujube', 'lemon', 'orange', 'tomato', 'banana', 'coconut', 'grape', 'pitaya'}


def cut_fruits(fruits):
    result = []
    for item in fruits:
        if item in FRUIT_NAMES:
            l = len(item)
            m = sum(divmod(l, 2))
            result.extend((item[:m], item[m:]))
        else:
            result.append(item)
    return result
