def done(w, seen):
    return w in seen


def size(w):
    return len(w) == len(set(w))


def check(w, word):
    found = False
    for (c1, c2) in zip(w, word):
        if c1 != c2:
            if found:
                return False
            else:
                found = True
    return True


def mutations(alice, bob, word, first):

    def okay(w):
        return not done(w, seen) and size(w) and check(w, word)

    def player():
        return bob if first else alice
    (seen, state) = ({word}, 0)
    while True:
        try:
            word = next(filter(okay, player()))
            if state == 1:
                return first
            if state == 0:
                state = 2
            seen.add(word)
        except:
            if state == 1:
                return -1
            if state == 2:
                return 1 - first
            if state == 0:
                state = 1
        first = 1 - first
