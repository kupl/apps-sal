def is_interesting(number, awesome_phrases):

    def check(n):
        nonlocal awesome_phrases
        n = str(n)

        def test0(x):
            return len(x) > 2

        def test1(x):
            return set(x[1:]) == set('0')

        def test2(x):
            return len(set(x)) == 1

        def test3(x):
            return all(((int(b) or 10) - (int(a) or 10) == 1 for (a, b) in zip(x, x[1:])))

        def test4(x):
            return all((int(a) - int(b) == 1 for (a, b) in zip(x, x[1:])))

        def test5(x):
            return x == x[::-1]

        def test6(x):
            return int(x) in awesome_phrases
        return test0(n) and (test1(n) or test2(n) or test3(n) or test4(n) or test5(n) or test6(n))
    return int(check(number) and 2 or (check(number + 1) or check(number + 2)))
