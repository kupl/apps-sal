def solve(arr):
    abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    res = []
    for el in arr:
        counter = 0
        for i in range(len(el)):
            if el.lower()[i] == abc[i]:
                counter += 1
        res.append(counter)
    return res
