# write the function is_anagram
def is_anagram(tst, org):
    tst = tst.lower()
    org = org.lower()
    if len(tst) != len(org):
        return False
    for i in org:
        if tst.count(i) != org.count(i):
            return False
    return True
