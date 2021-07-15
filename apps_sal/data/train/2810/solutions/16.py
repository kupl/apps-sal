def solve(arr):
    return [sum(ord(i.lower()) - 96 == indx for indx, i in enumerate(word, 1)) for word in arr]
