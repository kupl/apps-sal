from itertools import zip_longest

populate_dict = lambda keys, default: dict(zip_longest(keys, [default], fillvalue=default))
