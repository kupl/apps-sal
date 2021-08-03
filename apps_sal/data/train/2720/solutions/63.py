def solution(digits):
    if digits == "":
        return 0
    splice = 5
    lst = []
    for i, v in enumerate(digits):
        lst.append(digits[i:i + splice])
    maxval = (int(max(lst)))
    return maxval
