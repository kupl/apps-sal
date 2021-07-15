FRUIT_NAMES = {'blueberry', 'pear', 'durian', 'ginkgo', 'peach', 'apple', 'cantaloupe', 'fig', 'mangosteen', 'watermelon', 'pineapple', 'cherry', 'pomegranate', 'carambola', 'hawthorn', 'persimmon', 'apricot', 'plum', 'litchi', 'mango', 'jujube', 'lemon', 'orange', 'tomato', 'banana', 'coconut', 'grape', 'pitaya'}
def cut(x):
    if x in FRUIT_NAMES:
        m = (len(x) + 1) // 2
        return [x[:m], x[m:]]
    return [x]

def cut_fruits(fruits):
    return [x for xs in map(cut, fruits) for x in xs]
