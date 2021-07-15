from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
