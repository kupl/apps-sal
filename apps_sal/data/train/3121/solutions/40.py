def solve(arr):

    pos = [a for a in arr if a >= 0]
    neg = [a for a in arr if a < 0]

    neg = list(map(abs, neg))

    print(pos, neg)
    for element in arr:
        if not(abs(element) in pos and abs(element) in neg):
            return element
