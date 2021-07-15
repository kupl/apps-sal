from string import ascii_lowercase as al
def solve(arr):
    arr = map(str.lower,arr)
    result, counter = [], 0
    for word in arr:
        for i, c in enumerate(word):
            if i == al.index(c):
                counter += 1
        result.append(counter)
        counter = 0
    return result
