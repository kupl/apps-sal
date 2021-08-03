def cmp(a, b, f): return (a, b) == (0, 0) and -1 or a > b and 0 or a < b and 1 or a == b and not f and 1 or 0


def mutations(alice, bob, word, first):
    al, bo = 0, 0
    start = first
    seen = {word}

    def foo(alice, bob, word, first):
        nonlocal al, bo, start
        if first == 0:
            for a_word in alice:
                c1 = 0
                for i, x in enumerate(a_word):
                    if a_word[i] == word[i]:
                        c1 += 1

                if c1 == 3 and len(set(a_word)) == 4 and a_word not in seen:
                    seen.add(a_word)
                    word = a_word
                    al += 1
                    return foo(alice, bob, word, first + 1)

            if not al and not start:
                return foo(alice, bob, word, first + 1)

        else:
            for b_word in bob:
                c2 = 0
                for i, j in enumerate(b_word):
                    if b_word[i] == word[i]:
                        c2 += 1

                if c2 == 3 and len(set(b_word)) == 4 and b_word not in seen:
                    seen.add(b_word)
                    word = b_word
                    bo += 1
                    return foo(alice, bob, word, first - 1)

            if not bo and start:
                return foo(alice, bob, word, first - 1)

    foo(alice, bob, word, first)
    return cmp(al, bo, first)
