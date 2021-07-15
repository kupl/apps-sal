from string import ascii_lowercase

def solve(arr):
    return [
        sum(ascii_lowercase.index(c) == i for i, c in enumerate(word.lower()))
        for word in arr
    ]
