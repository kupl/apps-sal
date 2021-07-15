def case_sensitive(s):
    lst = [x for x in s if x.isupper()]
    return [len(lst) == 0, lst]
