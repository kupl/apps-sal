FRUIT_NAMES = {'blueberry', 'pear', 'durian', 'ginkgo', 'peach', 'apple', 'cantaloupe', 'fig', 'mangosteen', 'watermelon', 'pineapple', 'cherry', 'pomegranate', 'carambola', 'hawthorn', 'persimmon', 'apricot', 'plum', 'litchi', 'mango', 'jujube', 'lemon', 'orange', 'tomato', 'banana', 'coconut', 'grape', 'pitaya'}
F = {f: (f[:(len(f) + 1) // 2], f[(len(f) + 1) // 2:]) for f in FRUIT_NAMES}


def cut_fruits(fruits):
    return [e for t in [F.get(f, (f, '')) for f in fruits] for e in t if e]
