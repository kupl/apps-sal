def solve(arr):

    for n in arr:
        if n < 0 and abs(n) not in arr:
            return n
        elif n > 0 and -n not in arr:
            return n

