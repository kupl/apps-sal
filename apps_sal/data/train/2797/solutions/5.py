keys = ['123456789*0#', 'adgjmptw', 'behknqux', 'cfilorvy', 'sz']


def mobile_keyboard(s):
    return sum((i + 1 for (i, k) in enumerate(keys) for c in s if c in k))
