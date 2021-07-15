# write the function is_anagram
def is_anagram(test, original):
    t=test.lower()
    o=[*original.lower()]
    if len(t)!= len(o):
        return False
    for c in t:
        if c in o:
            o.remove(c)
        else:
            return False
    return True
