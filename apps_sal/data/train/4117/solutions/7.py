search = __import__("re").compile(r"\d+").findall


def sum_from_string(string):
    return sum(map(int, search(string)))
