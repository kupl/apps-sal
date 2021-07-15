def solve(s):
    for i in s:
        if i.isalpha():
            s = s.replace(i, " ")
    lst = s.split()
    largest = 0
    for w in lst:
        if int(w) > largest:
            largest = int(w)
    return largest
