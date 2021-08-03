import re


def partial_keys(d):
    class MyDict(dict):
        def __getitem__(self, item):
            for key in sorted(d):
                if re.match(item, key):
                    return d[key]
    return MyDict(**d)
