def order_weight(strng):
    return ' '.join(map(str, sorted(sorted(list(x for x in strng.split(" ") if x), key=lambda x: str(x)), key=lambda x: sum(map(int, str(x))))))
