from collections import Counter


def get_strings(city):
    return ",".join(f"{char}:{'*'*count}" for char, count in Counter(city.replace(" ", "").lower()).items())
