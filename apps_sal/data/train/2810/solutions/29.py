def solve(arr):
    s = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    res = []
    for el in arr:
        counter = 0
        for i in range(len(el)):
            if el.lower()[i] == s[i]:
                counter += 1
        res.append(counter)
    return res
