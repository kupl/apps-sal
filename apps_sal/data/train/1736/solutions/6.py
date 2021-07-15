def is_interesting(number, awesome_phrases):
    def check(n):
        nonlocal awesome_phrases
        n = str(n)
        test0 = lambda x: len(x) > 2
        test1 = lambda x: set(x[1:]) == set("0")
        test2 = lambda x: len(set(x)) == 1
        test3 = lambda x: all((int(b) or 10) - (int(a) or 10) == 1 for a, b in zip(x, x[1:]))
        test4 = lambda x: all(int(a) - int(b) == 1 for a, b in zip(x, x[1:]))
        test5 = lambda x: x == x[::-1]
        test6 = lambda x: int(x) in awesome_phrases
        return test0(n) and (test1(n) or test2(n) or test3(n) or test4(n) or test5(n) or test6(n))
    return int((check(number) and 2) or (check(number+1) or check(number+2)))
