def solve(arr):
    arrr = []
    for x in arr:
        res = 0
        start = ord('a')
        for y in x:
            if start == ord(y.lower()):
                res += 1
            start += 1
        arrr.append(res)
    return arrr
