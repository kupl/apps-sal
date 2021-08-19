def find_missing_number(s):
    try:
        lst = sorted(map(int, s.split()))
        return next((x for (x, y) in zip(range(1, lst[-1] + 1), lst) if x != y), 0)
    except IndexError:
        return 0
    except ValueError:
        return 1
