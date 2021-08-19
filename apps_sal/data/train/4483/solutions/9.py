FRUIT_NAMES = {'blueberry', 'pear', 'durian', 'ginkgo', 'peach', 'apple', 'cantaloupe', 'fig', 'mangosteen', 'watermelon', 'pineapple', 'cherry', 'pomegranate', 'carambola', 'hawthorn', 'persimmon', 'apricot', 'plum', 'litchi', 'mango', 'jujube', 'lemon', 'orange', 'tomato', 'banana', 'coconut', 'grape', 'pitaya'}


def cut_fruits(fruits):
    result = list()
    for val in fruits:
        if val in FRUIT_NAMES:
            if len(val) % 2 == 0:
                re = int(len(val) / 2)
                result.append(val[:re])
                result.append(val[re:])
            else:
                re = int(len(val) / 2)
                result.append(val[:re + 1])
                result.append(val[re + 1:])
        else:
            result.append(val)
    return result
