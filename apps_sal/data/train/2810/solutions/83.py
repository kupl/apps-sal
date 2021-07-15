import string
def solve(arr):
    return [(sum(1 for x in range(len(word)) if word.lower()[x] == string.ascii_letters[x])) for word in arr]
