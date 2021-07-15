def count_smileys(arr):
    import re
    smiley = re.compile(r"[:;][-~]?[)D]")
    return sum(bool(re.match(smiley, el)) for el in arr)
