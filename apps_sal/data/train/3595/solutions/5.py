def work_on_strings(a, b):
    return ''.join([elema if b.lower().count(elema.lower()) % 2 == 0 else elema.swapcase() for elema in a]) + ''.join([elemb if a.lower().count(elemb.lower()) % 2 == 0 else elemb.swapcase() for elemb in b])
