def solution(digits):
    if len(str(digits)) < 5:
        return digits
    string = str(digits)
    list2 = []
    maxi = len(string) - 4
    i = 0
    while i < maxi:
        for (s, x) in enumerate(string):
            list2.append(int(string[s:s + 5]))
            i = i + 1
    return max(list2)
